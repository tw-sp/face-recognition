import datetime as dt
import os
import random

from capture_images import takes_photos_in_web_cam
from index_images import index_images
from upload_files_to_s3 import upload_files_to_s3_bucket
from aws_config import *


def upload_face_to_rekognition_collection(list_of_image_filename, bucket_name):
    if isinstance(list_of_image_filename, list) and len(list_of_image_filename) > 0:
        remote_image_filenames = get_images_basenames(list_of_image_filename)
        remote_folder = str(dt.date.today()) + str(random.randint(0, 10000))

        list_of_uploaded_files = \
            upload_files_to_s3_bucket(bucket_name, list_of_image_filename, remote_image_filenames, remote_folder)

        return index_images(list_of_uploaded_files, bucket_name, COLLECTION_ID)


def upload_face_to_rekognition_collection_from_cam(bucket_name, image_name_prefix=""):
    captured_image_filenames = takes_photos_in_web_cam(image_name_prefix)
    return upload_face_to_rekognition_collection(captured_image_filenames, bucket_name)


def get_images_basenames(original_filenames_list):
    return [os.path.basename(filename) for filename in original_filenames_list]


if __name__ == "__main__":
    print upload_face_to_rekognition_collection_from_cam(BUCKET_NAME, "Deividas-")
