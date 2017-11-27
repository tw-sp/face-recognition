from aws_config import *
import os


def upload_files_to_s3_bucket(bucket_name, images, s3_keys, prefix=""):
    print ("UPLOAD TO S3 ==> Uploading to bucket %s" % bucket_name)
    print ("UPLOAD TO S3 ==> ")

    uploaded = []
    total_images = len(images)
    for image_index, image in enumerate(images):
        print ("UPLOAD TO S3 ==> Processing %d of %d" % (image_index + 1, total_images))

        uploaded_file = upload_file_to_s3_bucket(bucket_name, image, s3_keys[image_index], prefix)
        uploaded.append(uploaded_file)

    print("UPLOAD TO S3 ==> Complete")
    return uploaded


def upload_file_to_s3_bucket(bucket_name, image_name, s3_key, prefix=""):
    s3 = aws_session.resource('s3')
    s3_key_with_prefix = os.path.join(prefix, s3_key)
    s3.Bucket(bucket_name).upload_file(Key=s3_key_with_prefix, Filename=image_name)
    return s3_key_with_prefix
