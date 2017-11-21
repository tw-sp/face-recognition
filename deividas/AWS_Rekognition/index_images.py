import boto3
from capture_images import *

BUCKET_NAME = 'aiclub-testcollection1-bucket1'
COLLECTION_ID = 'testcollection1'
REGION="eu-west-1"
session = boto3.session.Session(profile_name='AIClub-AdminUser')
rekognition = session.client("rekognition", REGION)


def index_image(bucket, key, collection_id, external_image_id, attributes=()):
    response = rekognition.index_faces(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        CollectionId=collection_id,
        ExternalImageId=external_image_id,
        DetectionAttributes=attributes,
    )

    return response['FaceRecords']


def index_images_in_bucket(bucket, collection_id, prefix=""):
    images_in_bucket = get_images_in_bucket(bucket, prefix)
    results = []
    for image in images_in_bucket:
        index_image(bucket, image, collection_id, os.path.basename(image))
    return results


def get_images_in_bucket(bucket_name, prefix="", extension='.jpg'):
    s3 = session.resource('s3')
    all_files_in_bucket = s3.Bucket(bucket_name).objects.filter(Prefix=prefix)  # aiclub-testcollection1-bucket1
    images = [image.key for image in all_files_in_bucket if image.key.endswith(extension)]
    return images
