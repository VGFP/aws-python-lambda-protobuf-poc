import json
import boto3
import os


def lambda_handler(event, context):
    sqs_client = boto3.client("sqs")
    queue_url = os.environ["JSON_QUEUE_URL"]
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
    sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(data),
    )
    return {"statusCode": 200}
