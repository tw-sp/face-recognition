import boto3
import os

from capture_images import takes_photos_in_web_cam
from delete_files_from_s3 import delete_files_in_bucket
from upload_files_to_s3 import upload_file_to_s3_bucket

BUCKET_NAME = 'aiclub-testcollection1-bucket1'
COLLECTION_ID = 'testcollection1'
REGION="eu-west-1"
session = boto3.session.Session(profile_name='AIClub-AdminUser')
rekognition = session.client("rekognition", REGION)


def predict_identity_from_web_cam(bucket, collection_id, threshold=80, max_results=2):
    image_filename = takes_photos_in_web_cam(image_name_prefix="")[0]
    if len(image_filename) == 0:
        return
    print "Predicting %s" % image_filename
    s3_key = os.path.basename(image_filename)
    upload_file_to_s3_bucket(bucket, image_filename, s3_key=s3_key)
    identity_response = predict_identity_by_image(bucket, s3_key, collection_id, threshold, max_results)
    # delete_files_in_bucket(BUCKET_NAME, prefix=image_filename)
    return identity_response


def predict_identity_by_image(bucket, s3_key, collection_id, threshold=80, max_results=2):
    response = rekognition.search_faces_by_image(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": s3_key,
            }
        },
        CollectionId=collection_id,
        FaceMatchThreshold=threshold,
        MaxFaces=max_results
    )
    return response['FaceMatches']
