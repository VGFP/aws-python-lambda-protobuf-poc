import message_pb2
import base64


def lambda_handler(event, context):
    obj = message_pb2.MyMessage()
    obj.ParseFromString(base64.b64decode(event["body"]))
    return {"statusCode": 200}
