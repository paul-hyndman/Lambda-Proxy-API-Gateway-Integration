import json
import logging
import os
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    logging.getLogger().setLevel(level=os.getenv('LOG_LEVEL', 'DEBUG').upper())
    table_name = os.getenv('table_name')
    
    # Example of how when using API Proxy then requests are manually handled via code
    method = event["httpMethod"]
    if (method != 'POST'):
        return {
            'statusCode': 400,
            'body': 'Only supports HTTP POST'
        }
    
    # "body" attribute of event contains POST body
    body = json.loads(event["body"])
    
    orderId = body["orderId"]
    customerId = body["customerId"]
    sku = body["sku"]
    quantity = body["quantity"]
    
    client.put_item(
        TableName=table_name,
        Item={
            'order_id': {
            'S': orderId
            },
            'customer_id': {
            'S': customerId
            },
            'sku': {
            'S': sku
            },
            'quantity': {
            'S': str(quantity)
            }
        }
    )    
    
    print('Created order ' + json.dumps(body))
    
    return {
        'statusCode': 200,
        'body': 'Created order ' + json.dumps(body)
    }
