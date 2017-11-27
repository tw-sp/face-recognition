import json
from aws_config import *


def delete_files_in_bucket(bucket_name, prefix=""):
    s3 = aws_session.resource('s3')
    response = s3.Bucket(bucket_name).objects.filter(Prefix=prefix).delete()
    for part in response:
        return json.dumps(part, indent=2)
