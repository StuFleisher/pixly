from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db
import uuid
from models import Image

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
    unique_id = uuid.uuid1().hex
    print("ID>>>>>>",unique_id)
    new_image = Image(
    id = unique_id,
    make = request.form['make'],
    model = request.form['model'],
    date = request.form['date'],
    file_name = file.name,
    pixel_x_dimension = request.form['pixelXDimension'],
    pixel_y_dimension = request.form['pixelYDimension'],
    url= f'https://{BUCKET}.s3.amazonaws.com/{unique_id}.jpg'
    )
    db.session.add(new_image)
    db.session.commit()

    s3.Bucket(BUCKET).put_object(Key='test.jpg', Body=file)
    s3.Bucket(BUCKET).put_object(Key=f'{unique_id}.jpg', Body=file)

    return jsonify({"success": True})

@app.get('/image/<id>')
def get_image_by_id(id):
    image = Image.query.get(id)
    if image:
        return jsonify(image.serialized())
    else:
        return jsonify({"message":"Image is not found"})



