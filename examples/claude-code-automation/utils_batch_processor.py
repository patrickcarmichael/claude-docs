"""
Batch Processing Utility

Process multiple files or tasks in parallel using Claude Code.

This file should be placed at: utils/batch_processor.py
"""

import os
import time
from pathlib import Path
from typing import Callable, List, Optional, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

from claude_wrapper import generate, analyze_code, generate_tests


class BatchProcessor:
    """Process multiple items with Claude in parallel."""

    def __init__(
        self,
        max_workers: int = 4,
        delay_between_requests: float = 0.5,
        max_retries: int = 3,
        timeout: int = 300,
    ):
        """
        Initialize batch processor.

        Args:
            max_workers: Number of parallel workers
            delay_between_requests: Delay between API calls (seconds)
            max_retries: Number of retries on failure
            timeout: Request timeout (seconds)
        """
        self.max_workers = max_workers
        self.delay_between_requests = delay_between_requests
        self.max_retries = max_retries
        self.timeout = timeout
        self.request_count = 0
        self.error_count = 0

    def process_files(
        self,
        file_pattern: str,
        process_func: Callable,
        output_dir: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Process multiple files matching pattern.

        Args:
            file_pattern: Glob pattern for files
            process_func: Function to apply to each file
            output_dir: Directory to save results
            **kwargs: Additional arguments for process_func

        Returns:
            Dictionary with results and statistics
        """
        # Find files
        files = list(Path(".").glob(file_pattern))
        if not files:
            print(f"No files found matching: {file_pattern}")
            return {"results": {}, "stats": {"total": 0}}

        print(f"Found {len(files)} files to process")

        results = {}
        errors = {}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {}

            for file_path in files:
                # Submit task
                future = executor.submit(
                    self._process_file_with_retry,
                    file_path,
                    process_func,
                    kwargs
                )
                futures[future] = file_path

                # Add delay to avoid rate limiting
                time.sleep(self.delay_between_requests)

            # Process results as they complete
            for future in as_completed(futures):
                file_path = futures[future]
                try:
                    result = future.result(timeout=self.timeout)
                    results[str(file_path)] = result

                    if output_dir:
                        self._save_result(file_path, result, output_dir)

                    self.request_count += 1
                    print(f"✓ Processed: {file_path}")

                except Exception as e:
                    self.error_count += 1
                    errors[str(file_path)] = str(e)
                    print(f"✗ Failed: {file_path} - {e}")

        return {
            "results": results,
            "errors": errors,
            "stats": {
                "total": len(files),
                "successful": len(results),
                "failed": len(errors),
                "requests": self.request_count,
            }
        }

    def _process_file_with_retry(
        self,
        file_path: Path,
        process_func: Callable,
        kwargs: Dict
    ) -> Any:
        """Process a file with retry logic."""
        for attempt in range(self.max_retries):
            try:
                # Read file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Process
                result = process_func(content, **kwargs)
                return result

            except Exception as e:
                if attempt < self.max_retries - 1:
                    wait_time = (attempt + 1) * 2
                    print(f"  Retry {attempt + 1}/{self.max_retries} in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise

    def _save_result(
        self,
        file_path: Path,
        result: Any,
        output_dir: str
    ) -> None:
        """Save result to output directory."""
        os.makedirs(output_dir, exist_ok=True)

        # Generate output filename
        output_path = Path(output_dir) / file_path.name
        output_path = output_path.with_stem(output_path.stem + "_processed")

        # Save result
        with open(output_path, 'w', encoding='utf-8') as f:
            if isinstance(result, str):
                f.write(result)
            else:
                f.write(json.dumps(result, indent=2))


def process_for_analysis(
    file_pattern: str,
    output_file: Optional[str] = None,
    **kwargs
) -> None:
    """Analyze multiple files and generate report."""
    processor = BatchProcessor()

    results = processor.process_files(
        file_pattern,
        analyze_code,
        **kwargs
    )

    # Generate report
    report = []
    report.append("# Code Analysis Report\n")
    report.append(f"Total files: {results['stats']['total']}\n")
    report.append(f"Successful: {results['stats']['successful']}\n")
    report.append(f"Failed: {results['stats']['failed']}\n\n")

    report.append("## Results\n")
    for file_path, analysis in results["results"].items():
        report.append(f"\n### {file_path}\n")
        report.append(analysis)
        report.append("\n")

    if results["errors"]:
        report.append("\n## Errors\n")
        for file_path, error in results["errors"].items():
            report.append(f"- {file_path}: {error}\n")

    report_text = "".join(report)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(report_text)
        print(f"Report saved to: {output_file}")
    else:
        print(report_text)


def generate_tests_batch(
    file_pattern: str,
    output_dir: str = "./tests",
    **kwargs
) -> None:
    """Generate tests for multiple files."""
    processor = BatchProcessor()

    def generate_test_wrapper(code, **kw):
        return generate_tests(code, **kw)

    processor.process_files(
        file_pattern,
        generate_test_wrapper,
        output_dir=output_dir,
        **kwargs
    )

    print(f"Tests saved to: {output_dir}")


def refactor_batch(
    file_pattern: str,
    improvements: List[str],
    **kwargs
) -> None:
    """Refactor multiple files in place."""
    from claude_wrapper import refactor

    processor = BatchProcessor()

    def refactor_wrapper(code, **kw):
        return refactor(code, improvements, **kw)

    processor.process_files(
        file_pattern,
        refactor_wrapper,
        output_dir=None,  # Will overwrite original files
        **kwargs
    )

    print("Refactoring complete")


if __name__ == "__main__":
    # Example: Analyze all Python files
    print("Analyzing Python files...")
    process_for_analysis(
        "src/**/*.py",
        output_file="analysis_report.md",
        language="python"
    )
