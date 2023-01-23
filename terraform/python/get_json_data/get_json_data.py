import json
import sys

def lambda_handler(event, context):
    print(f'Received message size: {sys.getsizeof(event["Records"][0]["body"])}')
    obj = json.loads(event["Records"][0]["body"])
    return {"statusCode": 200}
