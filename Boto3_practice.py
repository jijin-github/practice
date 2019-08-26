import boto3

# client = boto3.client(
#     's3',
#     # Hard coded strings as credentials, not recommended.
#     aws_access_key_id='AKIARVRFM47R6KVLY2JC',
#     aws_secret_access_key='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'
# )
# rint s3.buckets.all()

client = boto3.resource('s3')

print client.buckets.all()