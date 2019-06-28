import boto3
import requests
import json
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    db=boto3.resource('dynamodb')
    table=db.Table("IFTTTimer_TimeTable")
    response = table.query(KeyConditionExpression=Key(X).eq(X) & Key("time").lte(int(datetime.now().timestamp())))
    print(response["Items"])
    for x in response["Items"]:
        requests.post(x['url'], data = json.dumps({
                "value1":"test"
            }))
        table.delete_item(Key={
            'time': int(x['time']), 
            'resource': x['resource']
        })
