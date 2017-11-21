import boto3
import os

BUCKET_NAME = 'aiclub-testcollection1-bucket1'
COLLECTION_ID = 'testcollection1'
REGION="eu-west-1"
session = boto3.session.Session(profile_name='AIClub-AdminUser')
rekognition = session.client("rekognition", REGION)


def upload_files_to_s3_bucket(bucket_name, images, s3_keys, prefix=""):
    uploaded = []
    for image_index, image in enumerate(images):
        uploaded_file = upload_file_to_s3_bucket(bucket_name, image, s3_keys[image_index], prefix)
        uploaded.append(uploaded_file)
    return uploaded


def upload_file_to_s3_bucket(bucket_name, image_name, s3_key, prefix=""):
    s3 = session.resource('s3')
    s3_key_with_prefix = os.path.join(prefix, s3_key)
    s3.Bucket(bucket_name).upload_file(Key=s3_key_with_prefix, Filename=image_name)
    return s3_key_with_prefix
