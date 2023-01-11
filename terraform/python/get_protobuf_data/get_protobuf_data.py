import message_pb2
import base64


def lambda_handler(event, context):
    obj = message_pb2.MyMessage()
    obj.ParseFromString(base64.b64decode(event["Records"][0]["body"]))
    for name in obj.DESCRIPTOR.fields_by_name:
        print(f"{name}: {getattr(obj, name)}")

    return {"statusCode": 200}
