import json

from predict_identity import predict_identity_from_web_cam
from aws_config import *


output = predict_identity_from_web_cam(BUCKET_NAME, COLLECTION_ID, threshold=DEFAULT_THRESHOLD)

print output
if output is None or len(output) == 0:
    print "No faces detected over set threshold(%d)" % DEFAULT_THRESHOLD

else:
    for part in output:
        print json.dumps(part, indent=2)
