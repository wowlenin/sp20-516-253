import json
import boto3
import os
import uuid

s3 = boto3.client("s3")
BUCKET = os.environ["BUCKET"]

def lambda_handler(event, context):
    response = s3.put_object(
            Body=json.dumps(event),
            Bucket=BUCKET,
            Key=str(uuid.uuid4())
        )
    print(response)
