import boto3


BUCKET_NAME = 'aiclub-testcollection1-bucket1'
COLLECTION_ID = 'testcollection1'
REGION="eu-west-1"
aws_session = boto3.session.Session(profile_name='AIClub-User')
rekognition_client = aws_session.client("rekognition", REGION)
DEFAULT_THRESHOLD = 80
