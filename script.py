import constants
import boto3
import requests

OBJECT_NAME_TO_UPLOAD = 'file_to_upload.jpg'

s3_client = boto3.client(
    's3',
    aws_access_key_id=constants.access_key,
    aws_secret_access_key=constants.secret_access_key
)

#Generate the presigned URL
response = s3_client.generate_presigned_post(
    Bucket = 'beabetterdev-presigned-demo',
    Key = OBJECT_NAME_TO_UPLOAD,
    ExpiresIn = 10 
)

print(response)

#Upload file to S3 using presigned URL
files = { 'file': open(OBJECT_NAME_TO_UPLOAD, 'rb')}
r = requests.post(response['url'], data=response['fields'], files=files)
print(r.status_code)
