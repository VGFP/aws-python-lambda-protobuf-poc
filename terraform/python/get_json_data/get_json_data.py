import json


def lambda_handler(event, context):
    obj = json.loads(event["Records"][0]["body"])
    return {"statusCode": 200}
