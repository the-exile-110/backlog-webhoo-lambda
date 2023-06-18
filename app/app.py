import json
import boto3


def lambda_handler(event, context):
    print("Event: ", event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
