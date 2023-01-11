import json


def lambda_handler(event, context):
    obj = json.loads(event["Records"][0]["body"])
    for key in obj.keys():
        print(f"{key}: {obj[key]}")
    return {"statusCode": 200}
