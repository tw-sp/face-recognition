from predict_identity import predict_identity_from_web_cam
import json
import boto3

BUCKET_NAME = 'aiclub-testcollection1-bucket1'
COLLECTION_ID = 'testcollection1'
REGION="eu-west-1"
session = boto3.session.Session(profile_name='AIClub-AdminUser')
rekognition = session.client("rekognition", REGION)

output = predict_identity_from_web_cam(BUCKET_NAME, COLLECTION_ID)

for part in output:
    print json.dumps(part, indent=2)