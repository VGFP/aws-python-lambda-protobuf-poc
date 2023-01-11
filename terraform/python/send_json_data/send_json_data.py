import json
import boto3
import os


def lambda_handler(event, context):
    sqs_client = boto3.client("sqs")
    queue_url = os.environ["JSON_QUEUE_URL"]
    sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps({"id": "123", "val1": "abc", "val2": 123, "val3": 1.116456456, "val4": False}),
    )
    return {"statusCode": 200}
