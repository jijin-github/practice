import boto3
from botocore.exceptions import ClientError

# How to create a client
client = boto3.client(
    'dynamodb',
    aws_access_key_id='AKIARVRFM47R6KVLY2JC',
    aws_secret_access_key='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',
    region_name='ap-south-1'
)


response = client.create_table(
	AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ],
    TableName='test1',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)