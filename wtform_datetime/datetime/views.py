from flask import Blueprint, render_template, request
from wtform_datetime.models import db, TimeStamp
from wtform_datetime.datetime.forms import DateTimeForm

datetime_blueprint = Blueprint(
    'datetime', __name__, template_folder="templates"
)


@datetime_blueprint.route('/', methods=["GET", "POST"])
def datetime_picker_demo():
    form = DateTimeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            dt = TimeStamp(datetime=form.datetime.data)
            db.session.add(dt)
            db.session.commit()
    return render_template('datetime.html', form=form)
