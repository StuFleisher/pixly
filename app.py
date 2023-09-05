from flask import Flask, request, jsonify
# import s3fs
import boto3
from dotenv import load_dotenv
import os

app = Flask(__name__)

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

s3.Bucket(BUCKET).upload_file(Filename="child.JPG", Key="child_file")

##############################################################################

@app.post('/add')
def store_img():
    print("Hello add route is being hit")
    file = request.files["image"]
    print(file)
    s3.Bucket(BUCKET).upload_file(Filename=file, Key="TestImage")
    return jsonify({"success": True})




