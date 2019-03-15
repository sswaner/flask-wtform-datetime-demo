from wtform_datetime import db
from sqlalchemy.dialects import postgresql


class TimeStamp(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(postgresql.TIMESTAMP(), nullable=False)
