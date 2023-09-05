from flask import Flask
import s3fs
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

AWS_ACCESS_KEY = os.getenv("aws_access_key_id")
SECRET_KEY = os.getenv("aws_secret_access_key")
BUCKET = os.getenv("bucket")

s3= boto3.resource(
    service_name="s3",
    region_name="us-east-1",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

s3.Bucket(BUCKET).upload_file(Filename="test.txt", Key="test_file")