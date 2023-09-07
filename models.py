from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Image(db.Model):

    __tablename__ = "images"

    id = db.Column(
        db.Integer,
        primary_key=True)

    file_name = db.Column(
        db.String,
        nullable=False)

    date = db.Column(
        db.String
    )

    pixel_x_dimension = db.Column(
        db.Integer
    )

    pixel_y_dimension = db.Column(
        db.Integer
    )

    make = db.Column(
        db.String()
    )

    model = db.Column(
        db.String()
    )

    url = db.Column(
        db.String()
    )

    def serialized(self):
        return {"id": self.id,
                "file_name": self.file_name,
                "date": self.date,
                "pixel_x_dimension": self.pixel_x_dimension,
                "pixel_y_dimension": self.pixel_y_dimension,
                "make": self.make,
                "model": self.model,
                "url": self.url
                }


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
