import os
import random

import boto3
import datetime as dt

from capture_images import takes_photos_in_web_cam
from delete_files_from_s3 import delete_files_in_bucket
from index_images import index_images_in_bucket
from upload_files_to_s3 import upload_files_to_s3_bucket

BUCKET_NAME = 'aiclub-testcollection1-bucket1'
COLLECTION_ID = 'testcollection1'
REGION="eu-west-1"
session = boto3.session.Session(profile_name='AIClub-AdminUser')
rekognition = session.client("rekognition", REGION)


def upload_face_to_rekognition_collection(list_of_image_filename):
    remote_image_filenames = get_images_basenames(list_of_image_filename)
    remote_folder = str(dt.date.today()) + str(random.randint(0, 10000))

    upload_files_to_s3_bucket(BUCKET_NAME, list_of_image_filename, remote_image_filenames, remote_folder)

    index_images_in_bucket(BUCKET_NAME, COLLECTION_ID, remote_folder)


def upload_face_to_rekognition_collection_from_cam(image_name_prefix=""):
    captured_image_filenames = takes_photos_in_web_cam(image_name_prefix)
    upload_face_to_rekognition_collection(captured_image_filenames)


def get_images_basenames(original_filenames_list):
    return [os.path.basename(filename) for filename in original_filenames_list]