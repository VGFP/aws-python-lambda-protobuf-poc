import large_message_pb2
import base64
import sys

def lambda_handler(event, context):
    print(f'Received message size: {sys.getsizeof(event["Records"][0]["body"])}')
    protobuf_obj = large_message_pb2.SomeMessage()
    protobuf_obj.ParseFromString(base64.b64decode(event["Records"][0]["body"]))

    return {"statusCode": 200}
