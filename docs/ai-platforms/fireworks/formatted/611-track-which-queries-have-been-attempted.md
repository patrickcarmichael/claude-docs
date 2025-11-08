---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Track which queries have been attempted

processed_query_indices = set()
retry_count = 0  # Track how many times we've cycled through all queries

iteration = 0
with duckdb.connect(SYNTHETIC_DB_PATH) as con:
    while iteration < MAX_ITERATIONS:
        iteration += 1
        
        # Get ALL current zero-result queries

        all_zero_indices = [i for i, q in enumerate(queries) if count_rows(con, q) == 0]
        zero_count = len(all_zero_indices)
        zero_percent = (zero_count / total_q * 100) if total_q else 0
        
        print(f"\n[Iteration {iteration}] Zero-result: {zero_count}/{total_q} ({zero_percent:.1f}%)")
        
        if zero_percent <= TARGET_MAX_ZERO_PERCENT or zero_count == 0:
            print(f"✅ Target achieved! {zero_percent:.1f}% <= {TARGET_MAX_ZERO_PERCENT}%")
            break
        
        # Get unprocessed zero-result queries

        unprocessed_zero_indices = [i for i in all_zero_indices if i not in processed_query_indices]
        
        # If we've processed all zero-result queries, reset to try stubborn ones again

        if not unprocessed_zero_indices and all_zero_indices:
            retry_count += 1
            print(f"  All zero-result queries have been attempted. Starting retry cycle #{retry_count}")
            processed_query_indices.clear()
            unprocessed_zero_indices = all_zero_indices
            
            # If we've done multiple retry cycles with no progress, stop

            if retry_count > 2:
                print(f"  Stopping after {retry_count} retry cycles")
                break
        
        # Take a batch of unprocessed queries

        batch_indices = unprocessed_zero_indices[:BATCH_SIZE]
        if not batch_indices:
            print(f"[Iteration {iteration}] No queries to process.")
            break
            
        batch_queries = [queries[i] for i in batch_indices]
        processed_query_indices.update(batch_indices)
        
        print(f"  Processing batch: queries {batch_indices[:3]}{'...' if len(batch_indices) > 3 else ''} ({len(batch_indices)} total)")
        
        # Group queries by their involved tables for efficient processing

        query_tables_map = defaultdict(list)
        for idx, q in zip(batch_indices, batch_queries):
            tables = extract_tables_from_query(q)
            if tables:
                # Create a key from sorted table names

                key = tuple(sorted(tables))
                query_tables_map[key].append((idx, q))
        
        if not query_tables_map:
            print(f"  No tables found in batch. Moving to next batch.")
            continue
        
        total_fixed = 0
        
        # Process each group of queries that share the same tables

        for table_tuple, query_list in query_tables_map.items():
            tables = list(table_tuple)
            query_indices = [idx for idx, _ in query_list]
            query_texts = [q for _, q in query_list]
            
            print(f"    Processing {len(query_list)} queries involving tables: {tables}")
            
            # Build Pydantic model

            RowsPayload = build_rows_payload_model(tables)
            rows_schema = RowsPayload.model_json_schema()
            
            # Limit rows per table

            props = rows_schema.get("properties", {})
            for t in list(props.keys()):
                spec = props.get(t, {})
                if isinstance(spec, dict) and spec.get("type") == "array":
                    spec["maxItems"] = min(MAX_ROWS_PER_TABLE_PER_BATCH, len(query_list))
            
            # Get sample data for context

            existing_samples = {}
            for t in tables:
                samples = get_sample_data(con, t, limit=5)
                if samples:
                    existing_samples[t] = samples
            
            # Analyze query patterns to understand what's needed

            query_analysis = []
            for q in query_texts[:3]:  # Analyze first 3 queries for brevity

                query_analysis.append(f"- {q}")
            
            system_prompt = """You are an expert at generating natural, realistic database records.
Generate minimal new rows that will make the provided SQL queries return results.
The data should be diverse, realistic, and consistent with the domain implied by the schema."""
            
            user_prompt = f"""
Given this DuckDB schema and SQL queries that return zero rows, generate the minimum number
of natural, realistic rows needed to make these queries return results.

**Database Schema:**
{schema_for_prompt}

**Tables to populate:** {json.dumps(tables)}

**Example existing data (for style/format reference):**
{json.dumps(existing_samples, indent=2, default=str) if existing_samples else "No existing samples available"}

**Queries that need to return results ({len(query_texts)} total):**
{chr(10).join(query_analysis)}
{f"... and {len(query_texts) - 3} more similar queries" if len(query_texts) > 3 else ""}

**Requirements:**
1. Generate at most {MAX_ROWS_PER_TABLE_PER_BATCH} rows per table
2. Make the data satisfy the WHERE conditions and JOINs in the queries
3. Use natural, realistic values appropriate for the domain
4. Maintain referential integrity between tables
5. Avoid duplicating existing IDs - generate new unique IDs
6. Create diverse data that satisfies multiple queries if possible

Return ONLY the JSON object with the new rows. No explanations.
""".strip()
            
            try:
                resp = llm.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    response_format={
                        "type": "json_schema",
                        "json_schema": {"name": "RowsPayload", "schema": rows_schema}
                    },
                    temperature=0.5,  # Some randomness for natural data

                )
                
                content = resp.choices[0].message.content
                if not content:
                    print(f"      Empty response from LLM")
                    continue
                
                payload = json.loads(content)
                
                # Insert generated rows

                rows_inserted = 0
                for t in tables:
                    rows = payload.get(t, [])
                    if not rows or not isinstance(rows, list):
                        continue
                    
                    # Convert to DataFrame

                    df = pd.DataFrame(rows[:MAX_ROWS_PER_TABLE_PER_BATCH])
                    cols = table_columns(t)
                    if not cols:
                        continue
                    
                    # Align columns

                    for c in cols:
                        if c not in df.columns:
                            df[c] = None
                    df = df[cols]
                    
                    # Insert new rows (avoiding exact duplicates)

                    try:
                        con.register("new_rows_df", df)
                        con.execute(f'INSERT INTO "{t}" SELECT * FROM new_rows_df EXCEPT SELECT * FROM "{t}"')
                        con.unregister("new_rows_df")
                        rows_inserted += len(df)
                    except Exception as e:
                        print(f"      Warning: Failed to insert into {t}: {e}")
                
                # Check how many queries were fixed

                fixed_in_group = 0
                for idx in query_indices:
                    if count_rows(con, queries[idx]) > 0:
                        fixed_in_group += 1
                
                print(f"      Inserted {rows_inserted} rows, fixed {fixed_in_group}/{len(query_list)} queries")
                total_fixed += fixed_in_group
                
            except Exception as e:
                print(f"      Error processing group: {e}")
                continue
            
            time.sleep(0.5)  # Rate limiting

        
        print(f"  [Iteration {iteration}] Total fixed in this iteration: {total_fixed} queries")
        
        # If we're in a retry cycle and made no progress, stop

        if retry_count > 0 and total_fixed == 0:
            print(f"  No progress made in retry cycle. Stopping.")
            break

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
