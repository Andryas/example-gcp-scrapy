from google.cloud import storage
from dotenv import load_dotenv
from os import getenv

import json

load_dotenv()

def upload_blob(bucket_name, source, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"
    storage_client = storage.Client.from_service_account_json(getenv("GOOGLE_APPLICATION_CREDENTIALS"))   

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    if isinstance(source, dict):
        blob.upload_from_string(data=json.dumps(source),content_type='application/json') 
        print(
            f"Dictionary uploaded to {destination_blob_name}."
        )
    elif isinstance(source, str):
        blob.upload_from_filename(source)
        print(
            f"File {source} uploaded to {destination_blob_name}."
        )
    else:
        print(
            "Please source must be a file path or a dictionary"
        )

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client.from_service_account_json(getenv("GOOGLE_APPLICATION_CREDENTIALS")) 

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print(f"Blob {blob_name} deleted.")

def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client.from_service_account_json(getenv("GOOGLE_APPLICATION_CREDENTIALS")) 
    buckets = storage_client.list_buckets()

    names = []
    for bucket in buckets:
        # printæ(bucket.name)
        names.append(bucket.name)
    
    return names

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client.from_service_account_json(getenv("GOOGLE_APPLICATION_CREDENTIALS")) 

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    names = []
    for blob in blobs:
        # print(blob.name)
        names.append(blob.name)
    return names