import os
import boto3
import large_message_pb2
import base64


def get_protobuf() -> large_message_pb2.SomeMessage:
    protobuf_obj = large_message_pb2.SomeMessage()

    previews_obj = protobuf_obj.Previews()
    previews_obj.url = "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview118/v4/14/d3/a1/14d3a1b9-9a2e-2b3d-3a3f-c3af1d7e9e5a/mzaf_6244467020788691521.plus.aac.p.m4a"

    artwark_obj = protobuf_obj.Artwork()
    artwark_obj.width = 3000
    artwark_obj.height = 3000
    artwark_obj.url = r"https://is5-ssl.mzstatic.com/image/thumb/Music118/v4/a5/5f/0d/a55f0df9-b9e8-a15d-f2f2-c3a3f8f9e5b1/093624901609.jpg/{w}x{h}bb.jpeg"
    artwark_obj.bgColor = "f5e9e9"
    artwark_obj.textColor1 = "1b2120"
    artwark_obj.textColor2 = "4f4f4f"
    artwark_obj.textColor3 = "3e3e3e"
    artwark_obj.textColor4 = "c5c5c5"

    attributes_obj = protobuf_obj.Attributes()
    attributes_obj.artistName = "Adele"
    attributes_obj.name = "Hello"
    attributes_obj.albumName = "25"
    attributes_obj.trackNumber = 1
    attributes_obj.genreNames.extend(["Pop", "Music"])
    attributes_obj.durationInMillis = 288000
    attributes_obj.releaseDate = "2015-10-23"
    attributes_obj.isrc = "GBBKS1500213"
    attributes_obj.contentRating = "clean"
    attributes_obj.previews.extend([previews_obj])
    attributes_obj.artwork.CopyFrom(artwark_obj)

    data_obj = protobuf_obj.Data()
    data_obj.id = "1516861207"
    data_obj.type = "songs"
    data_obj.href = "/v1/catalog/us/songs/1516861207"
    data_obj.attributes.CopyFrom(attributes_obj)

    paging_obj = protobuf_obj.Paging()
    paging_obj.offset = 0
    paging_obj.limit = 1

    meta_obj = protobuf_obj.Meta()
    meta_obj.paging.CopyFrom(paging_obj)

    protobuf_obj.data.extend([data_obj])
    protobuf_obj.meta.CopyFrom(meta_obj)

    return protobuf_obj


def lambda_handler(event, context):
    sqs_client = boto3.client("sqs")
    queue_url = os.environ["PROTOBUF_QUEUE_URL"]
    protobuf_obj = get_protobuf()
    sqs_client.send_message(QueueUrl=queue_url, MessageBody=base64.b64encode(protobuf_obj.SerializeToString()).decode("utf-8"))
    return {"statusCode": 200}
