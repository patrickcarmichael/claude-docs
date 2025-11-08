---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `S3ReaderTool` uses the AWS SDK for Python (boto3) to interact with S3:

```python Code theme={null}
class S3ReaderTool(BaseTool):
    name: str = "S3 Reader Tool"
    description: str = "Reads a file from Amazon S3 given an S3 file path"
    
    def _run(self, file_path: str) -> str:
        try:
            bucket_name, object_key = self._parse_s3_path(file_path)

            s3 = boto3.client(
                's3',
                region_name=os.getenv('CREW_AWS_REGION', 'us-east-1'),
                aws_access_key_id=os.getenv('CREW_AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('CREW_AWS_SEC_ACCESS_KEY')
            )

            # Read file content from S3
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            file_content = response['Body'].read().decode('utf-8')

            return file_content
        except ClientError as e:
            return f"Error reading file from S3: {str(e)}"
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Error Handling](./760-error-handling.md)

**Next:** [Conclusion →](./762-conclusion.md)
