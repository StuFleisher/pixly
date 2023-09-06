from flask import Flask, request, jsonify
# import s3fs
from flask_cors import CORS
import boto3
from dotenv import load_dotenv
import os

app = Flask(__name__)
# CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])
CORS(app)


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

##############################################################################

@app.post('/add')
def store_img():
    print("Hello add route is being hit")
    print(request)
    file = request.files["file"]
    print("\n\n\n\n*******",file)
    s3.Bucket(BUCKET).put_object(Key=file.filename, Body=file)
    return jsonify({"success": True})




