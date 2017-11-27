from capture_images import *
from aws_config import *


def index_image(bucket, key, collection_id, external_image_id, attributes=()):
    response = rekognition_client.index_faces(
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
    list_of_images = get_images_in_bucket(bucket, prefix)
    index_images(list_of_images, bucket, collection_id)


def index_images(list_of_images, bucket, collection_id):
    print ("INDEXING ==> Indexing to Collection: %s " % collection_id)
    print ("INDEXING ==> Indexing from Bucket: %s" % bucket)
    print ("INDEXING ==>")

    results = []
    total_images = len(list_of_images)
    for image_index, image in enumerate(list_of_images):
        print ("INDEXING ==> Processing %d of %d" % (image_index + 1, total_images))
        response = index_image(bucket, image, collection_id, os.path.basename(image))
        results.append(response)
    print("INDEXING ==> Complete")
    return results


def get_images_in_bucket(bucket_name, prefix="", extension='.jpg'):
    s3 = aws_session.resource('s3')
    all_files_in_bucket = s3.Bucket(bucket_name).objects.filter(Prefix=prefix)  # aiclub-testcollection1-bucket1
    images = [image.key for image in all_files_in_bucket if image.key.endswith(extension)]
    return images
