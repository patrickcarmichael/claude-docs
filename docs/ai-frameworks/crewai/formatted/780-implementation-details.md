---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `S3WriterTool` uses the AWS SDK for Python (boto3) to interact with S3:

```python Code theme={null}
class S3WriterTool(BaseTool):
    name: str = "S3 Writer Tool"
    description: str = "Writes content to a file in Amazon S3 given an S3 file path"
    
    def _run(self, file_path: str, content: str) -> str:
        try:
            bucket_name, object_key = self._parse_s3_path(file_path)

            s3 = boto3.client(
                's3',
                region_name=os.getenv('CREW_AWS_REGION', 'us-east-1'),
                aws_access_key_id=os.getenv('CREW_AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('CREW_AWS_SEC_ACCESS_KEY')
            )

            s3.put_object(Bucket=bucket_name, Key=object_key, Body=content.encode('utf-8'))
            return f"Successfully wrote content to {file_path}"
        except ClientError as e:
            return f"Error writing file to S3: {str(e)}"
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Error Handling](./779-error-handling.md)

**Next:** [Conclusion →](./781-conclusion.md)
