import os
import boto3
import message_pb2
import base64


def lambda_handler(event, context):
    sqs_client = boto3.client("sqs")
    queue_url = os.environ["PROTOBUF_QUEUE_URL"]
    obj = message_pb2.MyMessage()
    obj.id = "123"
    obj.val1 = "abc"
    obj.val2 = 123
    obj.val3 = 1.116456456
    obj.val4 = False
    sqs_client.send_message(QueueUrl=queue_url, MessageBody=base64.b64encode(obj.SerializeToString()).decode())
