import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

bucket = os.getenv('S3_BUCKET')

def upload_event_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    print(f"📤 Uploading: {folder_name}")
    for file in os.listdir(folder_path):
        if file.endswith('.mp4'):
            file_path = os.path.join(folder_path, file)
            s3_key = f"{folder_name}/{file}"
            s3.upload_file(file_path, bucket, s3_key)
            print(f"✅ Uploaded {file} to {bucket}/{s3_key}")