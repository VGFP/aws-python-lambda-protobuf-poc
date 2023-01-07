import json

def lambda_handler(event, context):
    obj = json.loads(event["body"])
    return {"statusCode": 200}