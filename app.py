from flask import Flask, request, jsonify
# import s3fs
from flask_cors import CORS
import boto3
from dotenv import load_dotenv
import os
# import psycopg2-binary
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///pixly")

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
connect_db(app)



@app.post('/add')
def store_img():
    print("Hello add route is being hit")
    print(request)
    file = request.files["file"]
    print("FILENAME>>>>", file.name)

    print("\n\n\n\n*******",file)
    print("request.form>>>>", request.form)
    make = request.form['make']
    print("make>>>>", make)

    s3.Bucket(BUCKET).put_object(Key='test.jpg', Body=file)
    s3.Bucket(BUCKET).put_object(Key=file.filename, Body=file)
    return jsonify({"success": True})




