import json

import boto3


BUCKET_NAME = 'aiclub-testcollection1-bucket1'
COLLECTION_ID = 'testcollection1'
REGION="eu-west-1"
session = boto3.session.Session(profile_name='AIClub-AdminUser')
rekognition = session.client("rekognition", REGION)


def delete_files_in_bucket(bucket_name, prefix=""):
    s3 = session.resource('s3')
    response = s3.Bucket(bucket_name).objects.filter(Prefix=prefix).delete()
    for part in response:
        return json.dumps(part, indent=2)
