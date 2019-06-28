import json
from datetime import datetime
import boto3

def lambda_handler(event, context):
    print(event)
    body=json.loads(event["body"])
    timer_time=int(datetime.now().timestamp())+int(body["time"])
    url=body["url"]
    db = boto3.resource('dynamodb')
    table = db.Table('IFTTTimer_TimeTable')
    response = table.put_item(
        Item={
            "time":timer_time,
            "resource":event['resource'],
            "url":url
        }
    )