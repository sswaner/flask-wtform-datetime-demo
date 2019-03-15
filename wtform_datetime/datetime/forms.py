from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateTimeField
from wtforms.validators import DataRequired


class DateTimeForm(FlaskForm):
    datetime = DateTimeField(
        'Date and Time',
        validators=[DataRequired('Provide a valid date and time!')],
        format='%Y/%m/%d %I:%M:%S %p'
    )
