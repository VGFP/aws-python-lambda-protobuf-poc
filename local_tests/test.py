import message_pb2
import json
import base64
import time
import codecs


def test_protobuf_decode(event: dict) -> None:
    obj = message_pb2.MyMessage()
    obj.ParseFromString(base64.b64decode(event["body"]))
    return
    # for key, value in obj.ListFields():
    #     print(key.name, value)


def test_json_decode(event: dict) -> None:
    obj = json.loads(event["body"])
    return
    # for key, value in event.items():
    #     print(key, value)


def decode_test():
    test_num = 1000000

    json_time_start = time.time()

    for i in range(test_num):
        test_json_decode(event= {
            "resource": "Resource path",
            "path": "Path parameter",
            "httpMethod": "Incoming request's method name",
            "headers": "{Incoming request headers}",
            "queryStringParameters": "{query string parameters}",
            "pathParameters":  "{path parameters}",
            "stageVariables": "{Applicable stage variables}",
            "requestContext": "{Request context, including the function name and ARN}",
            "body": '{"id": "123", "val1": "abc", "val2": 123, "val3": 1.116456456, "val4": false}',
            "isBase64Encoded": "A boolean flag indicating whether the `body` is base64-encoded"
        })

    json_time_end = time.time()

    json_time_diff = json_time_end - json_time_start

    protobuf_time_start = time.time()

    for i in range(test_num):
        test_protobuf_decode(event= 
            {
                "resource": "Resource path",
                "path": "Path parameter",
                "httpMethod": "Incoming request's method name",
                "headers": "{Incoming request headers}",
                "queryStringParameters": "{query string parameters}",
                "pathParameters":  "{path parameters}",
                "stageVariables": "{Applicable stage variables}",
                "requestContext": "{Request context, including the function name and ARN}",
                "body": "CgMxMjMSA2FiYxh7IVnZ3nEB3fE/",
                "isBase64Encoded": "A boolean flag indicating whether the `body` is base64-encoded"
            }
        )

    protobuf_time_end = time.time()

    protobuf_time_diff = protobuf_time_end - protobuf_time_start

    print("Protobuf time: ", protobuf_time_diff)
    print("JSON time: ", json_time_diff)
    print(f"Diff proto - josn: {protobuf_time_diff - json_time_diff}")


def encode_test():
    message_dict = {"id": "123", "val1": "abc", "val2": 123, "val3": 1.116456456, "val4": False}

    test_num = 1000000

    json_time_start = time.time()

    for i in range(test_num):
        test_json_encode(message_dict)
    
    json_time_end = time.time()

    json_time_diff = json_time_end - json_time_start

    protobuf_time_start = time.time()

    for i in range(test_num):
        test_protobuf_encode(message_dict)

    protobuf_time_end = time.time()

    protobuf_time_diff = protobuf_time_end - protobuf_time_start

    print("Encode Protobuf time: ", protobuf_time_diff)
    print("Encode JSON time: ", json_time_diff)
    print(f"Encode Diff proto - josn: {protobuf_time_diff - json_time_diff}")


def test_protobuf_encode(obj: dict) -> None:
    protobuf_obj = message_pb2.MyMessage()
    protobuf_obj.id = obj["id"]
    protobuf_obj.val1 = obj["val1"]
    protobuf_obj.val2 = obj["val2"]
    protobuf_obj.val3 = obj["val3"]
    protobuf_obj.val4 = obj["val4"]
    base64.b64encode(protobuf_obj.SerializeToString())
    return


def test_json_encode(obj: dict) -> None:
    json.dumps(obj)
    return


def main():
    decode_test()
    encode_test()


if __name__ == "__main__":
    main()
    