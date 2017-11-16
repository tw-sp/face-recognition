import boto3

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


def index_all_images_in_bucket(bucket, collection_id):
    images_in_bucket = get_images_in_bucket(bucket)
    results = [index_image(bucket, image, collection_id, get_filename_with_extension(image)) for image in images_in_bucket]
    return results


def get_filename_with_extension(path):
    return path.split('/')[-1]


def get_images_in_bucket(bucketName, extension='.jpg'):
    s3 = session.resource('s3')
    all_files_in_bucket = s3.Bucket(bucketName).objects.all() # aiclub-testcollection1-bucket1
    images = [image.key for image in all_files_in_bucket if image.key.endswith(extension)]
    return images


def search_faces_by_image(bucket, image, collection_id, threshold=80, max_results=2):
    response = rekognition.search_faces_by_image(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": image,
            }
        },
        CollectionId=collection_id,
        FaceMatchThreshold=threshold,
        MaxFaces=max_results
    )
    return response['FaceMatches']


def upload_images_to_S3_bucket(bucket, image):
    pass


def delete_images_from_S3_bucket(bucket, image):
    pass

def upload_face_to_collection():
    pass

if __name__ == "__main__":
    for record in search_faces_by_image(BUCKET_NAME, 'celebA-align/Deividas10.jpg', COLLECTION_ID):
        face = record['Face']
        print "Matched Face ({}%)".format(record['Similarity'])
        print "  FaceId : {}".format(face['FaceId'])
        print "  ImageId : {}".format(face['ExternalImageId'])