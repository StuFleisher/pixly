from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Image(db.Model):

    __tablename__= "images"

    id= db.Column(
        db.Integer,
        primary_key=True)

    file_name= db.Column(
        db.String,
        nullable = False)

    date= db.Column(
        db.String
    )

    pixel_x_dimension= db.Column(
        db.Integer
    )

    pixel_y_dimension= db.Column(
        db.Integer
    )

    make = db.Column(
        db.String()
    )

    model = db.Column(
        db.String()
    )

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
