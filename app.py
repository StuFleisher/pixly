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
    # print("ID>>>>>>",unique_id)
    print(request.form)

    new_image = Image(
    id = unique_id, #request.form['id'],
    make = request.form.get('make'),
    model = request.form.get('model') ,
    date = request.form.get('date'),
    file_name = request.form.get("file_name"),
    pixel_x_dimension = request.form.get('pixelXDimension'),
    pixel_y_dimension = request.form.get('pixelYDimension'),
    url= f'https://{BUCKET}.s3.amazonaws.com/{unique_id}.jpg'
    )
    db.session.add(new_image)
    db.session.commit()

    s3.Bucket(BUCKET).put_object(Key=f'{unique_id}.jpg', Body=file)

    return jsonify({"image": new_image.serialized()})



@app.get('/image/<id>')
def get_image_by_id(id):
    image = Image.query.get(id)
    if image:
        return jsonify(image.serialized())
    else:
        return jsonify({"message":"Image is not found"})



@app.patch('/image/<id>/edit')
def update_image(id):
    # allows for updating of the image only
    
    file = request.files["file"]
    image = Image.query.get(id)
    s3.Bucket(BUCKET).put_object(Key=f'{image.id}.jpg', Body=file)

    return jsonify({"image": image.serialized()})


@app.get('/images')
def get_all_images():
    images = Image.query.all()
    serialized_images = [image.serialized() for image in images]
    return jsonify({"images":serialized_images})



