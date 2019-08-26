import boto3

# client = boto3.client(
#     's3',
#     # Hard coded strings as credentials, not recommended.
#     aws_access_key_id='',
#     aws_secret_access_key=''
# )
# rint s3.buckets.all()

client = boto3.resource('s3')

print client.buckets.all()
