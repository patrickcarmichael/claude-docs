---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## credentials_file = "populate if you are running in a non Vertex AI environment."

gcs_input_prefix = ""


def batch_process_documents(
    project_id: str,
    location: str,
    processor_id: str,
    gcs_output_uri: str,
    gcs_input_prefix: str,
    timeout: int = 400
) -> None:
    parsed_documents = []

    # Client configs

    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    # With credentials

    # opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com", credentials_file=credentials_file)

    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    processor_name = client.processor_path(project_id, location, processor_id)

    # Input storage configs

    gcs_prefix = documentai.GcsPrefix(gcs_uri_prefix=gcs_input_prefix)
    input_config = documentai.BatchDocumentsInputConfig(gcs_prefix=gcs_prefix)

    # Output storage configs

    gcs_output_config = documentai.DocumentOutputConfig.GcsOutputConfig(gcs_uri=gcs_output_uri, field_mask=None)
    output_config = documentai.DocumentOutputConfig(gcs_output_config=gcs_output_config)
    storage_client = storage.Client()
    # With credentials

    # storage_client = storage.Client.from_service_account_json(json_credentials_path=credentials_file)

    # Batch process docs request

    request = documentai.BatchProcessRequest(
        name=processor_name,
        input_documents=input_config,
        document_output_config=output_config,
    )

    # batch_process_documents returns a long running operation

    operation = client.batch_process_documents(request)

    # Continually polls the operation until it is complete.

    # This could take some time for larger files

    try:
        print(f"Waiting for operation {operation.operation.name} to complete...")
        operation.result(timeout=timeout)
    except (RetryError, InternalServerError) as e:
        print(e.message)

    # Get output document information from completed operation metadata

    metadata = documentai.BatchProcessMetadata(operation.metadata)
    if metadata.state != documentai.BatchProcessMetadata.State.SUCCEEDED:
        raise ValueError(f"Batch Process Failed: {metadata.state_message}")

    print("Output files:")
    # One process per Input Document

    for process in list(metadata.individual_process_statuses):
        matches = re.match(r"gs://(.*?)/(.*)", process.output_gcs_destination)
        if not matches:
            print("Could not parse output GCS destination:", process.output_gcs_destination)
            continue

        output_bucket, output_prefix = matches.groups()
        output_blobs = storage_client.list_blobs(output_bucket, prefix=output_prefix)

        # Document AI may output multiple JSON files per source file

        # (Large documents get split in multiple file "versions" doc --> parsed_doc_0 + parsed_doc_1 ...)

        for blob in output_blobs:
            # Document AI should only output JSON files to GCS

            if blob.content_type != "application/json":
                print(f"Skipping non-supported file: {blob.name} - Mimetype: {blob.content_type}")
                continue

            # Download JSON file as bytes object and convert to Document Object

            print(f"Fetching {blob.name}")
            document = documentai.Document.from_json(blob.download_as_bytes(), ignore_unknown_fields=True)
            # Store the filename and the parsed versioned document content as a tuple

            parsed_documents.append((blob.name.split("/")[-1].split(".")[0], document.text))

    print("Finished document parsing process.")
    return parsed_documents

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
