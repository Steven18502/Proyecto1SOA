# [START vision_face_detection_gcs]
def detect_faces_cloud():
    """Detects faces in the file located in Google Cloud Storage or the web."""
    from google.cloud import vision 
    from google.cloud import storage
    
    # Activate Google vision API using service account key
    client = vision.ImageAnnotatorClient.from_service_account_json(apikey)
    
    # Get GCS bucket
    storage_client = storage.Client.from_service_account_json(apikey)
    bucket = storage_client.bucket(bucketname)
    
    # Get images paths (only one MUST be in bucket)
    blob_list = list(bucket.list_blobs())
    blob_name = blob_list[0].name
    print(f"Blob: {blob_name} analize.")
    image_path = "gs://{0}/{1}".format(bucketname, blob_name)

    # [START vision_python_migration_image_uri]
    image = vision.Image()
    image.source.image_uri = image_path
    # [END vision_python_migration_image_uri]

    # API face detection response
    response = client.face_detection(image=image)
    
    # Face expression detection
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
    
    emotions_json = []
    if faces:
        for index, face in enumerate(faces):
            emotions = []
            emotions.append(index+1)
            emotions.append(likelihood_name[face.joy_likelihood])
            emotions.append(likelihood_name[face.sorrow_likelihood])
            emotions.append(likelihood_name[face.anger_likelihood])
            emotions.append(likelihood_name[face.surprise_likelihood])
            emotions_json.append(emotions)
            show(emotions)
    
    # Delete the analyzed image.
    delete_blob(bucket, blob_name)
    
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
# [END vision_face_detection_gcs]


def delete_blob(bucket, blob_name):
    """Deletes a blob from the bucket."""
    blob = bucket.blob(blob_name)
    # blob.delete()
    print(f"Blob: {blob_name} deleted.")

# Function that prints the emotion to the terminal.
# INPUT: emotions array.
# OUTPUT: print the values with respective labels.
def show(emotions):
    import json
    data = {}
    data['face'] = emotions[0]
    data['joy'] = emotions[1]
    data['sorrow'] = emotions[2]
    data['anger'] = emotions[3]
    data['surpirse'] = emotions[4]
    json_data = json.dumps(data)

    print("\nFace", emotions[0])
    print('joy: {}'.format(emotions[1]))
    print('sorrow: {}'.format(emotions[2]))
    print('anger: {}'.format(emotions[3]))
    print('surprise: {}'.format(emotions[4]))
    print('json {}\n'.format(json_data))

if __name__ == "__main__":
    apikey = "apikey.json"
    bucketname = "soa-visionapi-bucket"
    detect_faces_cloud()