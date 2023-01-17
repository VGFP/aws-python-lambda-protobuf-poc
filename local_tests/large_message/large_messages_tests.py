import json
import large_message_pb2
import time
import base64
from pprint import pprint


def get_protobuf() -> large_message_pb2.SomeMessage:
    protobuf_obj = large_message_pb2.SomeMessage()

    previews_obj = protobuf_obj.Previews()
    previews_obj.url = "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview118/v4/14/d3/a1/14d3a1b9-9a2e-2b3d-3a3f-c3af1d7e9e5a/mzaf_6244467020788691521.plus.aac.p.m4a"

    artwark_obj = protobuf_obj.Artwork()
    artwark_obj.width = 3000
    artwark_obj.height = 3000
    artwark_obj.url = "https://is5-ssl.mzstatic.com/image/thumb/Music118/v4/a5/5f/0d/a55f0df9-b9e8-a15d-f2f2-c3a3f8f9e5b1/093624901609.jpg/{w}x{h}bb.jpeg"
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


def print_protobuf(protobuf_obj: large_message_pb2.SomeMessage) -> None:
    print(protobuf_obj.data[0])
    print("Meta: {" + f"\n  Limit: {protobuf_obj.meta.paging.limit}")
    print(f"  Offset: {protobuf_obj.meta.paging.offset}" + "\n}")


def get_json() -> str:
    data = {
        "data": [
            {
                "id": "1516861207",
                "type": "songs",
                "href": "/v1/catalog/us/songs/1516861207",
                "attributes": {
                    "previews": [
                        {
                            "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview118/v4/14/d3/a1/14d3a1b9-9a2e-2b3d-3a3f-c3af1d7e9e5a/mzaf_6244467020788691521.plus.aac.p.m4a"
                        }
                    ],
                    "artwork": {
                        "width": 3000,
                        "height": 3000,
                        "url": "https://is5-ssl.mzstatic.com/image/thumb/Music118/v4/a5/5f/0d/a55f0df9-b9e8-a15d-f2f2-c3a3f8f9e5b1/093624901609.jpg/{w}x{h}bb.jpeg",
                        "bgColor": "f5e9e9",
                        "textColor1": "1b2120",
                        "textColor2": "4f4f4f",
                        "textColor3": "3e3e3e",
                        "textColor4": "c5c5c5",
                    },
                    "artistName": "Adele",
                    "name": "Hello",
                    "albumName": "25",
                    "trackNumber": 1,
                    "genreNames": ["Pop", "Music"],
                    "durationInMillis": 288000,
                    "releaseDate": "2015-10-23",
                    "isrc": "GBBKS1500213",
                    "contentRating": "clean",
                },
            }
        ],
        "meta": {"paging": {"limit": 1, "offset": 0}},
    }
    return json.dumps(data)


def print_json(json_str: str) -> None:
    print(json.loads(json_str))


def encode_json(json_str: dict) -> str:
    return json.dumps(json_str)


def decode_json(json_str: str) -> dict:
    return json.loads(json_str)


def encode_protobuf(protobuf_obj: large_message_pb2.SomeMessage) -> str:
    return base64.b64encode(protobuf_obj.SerializeToString()).decode("utf-8")


def decode_protobuf(protobuf_str: str) -> large_message_pb2.SomeMessage:
    protobuf_obj = large_message_pb2.SomeMessage()
    protobuf_obj.ParseFromString(base64.b64decode(protobuf_str))
    return protobuf_obj


def test_json() -> dict:
    json_str = get_json()
    start = time.time()
    for i in range(1000000):
        encode_json(json_str)
    end = time.time()
    print(f"JSON encoding: {end - start}")
    encode_json_time = end - start

    start = time.time()
    for i in range(1000000):
        decode_json(json_str)
    end = time.time()
    print(f"JSON decoding: {end - start}")
    decode_json_time = end - start

    return {"encode_json": encode_json_time, "decode_json": decode_json_time}


def test_protobuf() -> dict:

    protobuf_obj = get_protobuf()
    str_obj = base64.b64encode(protobuf_obj.SerializeToString()).decode("utf-8")

    start = time.time()
    for i in range(1000000):
        encode_protobuf(protobuf_obj)
    end = time.time()
    print(f"Protobuf encoding: {end - start}")
    encode_protobuf_time = end - start

    start = time.time()
    for i in range(1000000):
        decode_protobuf(str_obj)
    end = time.time()
    print(f"Protobuf decoding: {end - start}")
    decode_protobuf_time = end - start

    return {"encode_protobuf": encode_protobuf_time, "decode_protobuf": decode_protobuf_time}


def main():
    json_res = test_json()
    protobuf_res = test_protobuf()
    print(f"encoding diff: {json_res['encode_json'] - protobuf_res['encode_protobuf']}")
    print(f"encoding protobuf / json: {protobuf_res['encode_protobuf'] / json_res['encode_json']}")
    print(f"decoding diff: {json_res['decode_json'] - protobuf_res['decode_protobuf']}")
    print(f"decoding protobuf / json: {protobuf_res['decode_protobuf'] / json_res['decode_json']}")

    # protobuf_obj = get_protobuf()
    # print_protobuf(protobuf_obj=protobuf_obj)

    # json_str = get_json()
    # print_json(json_str=json_str)


if __name__ == "__main__":
    main()
