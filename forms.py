from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    company = StringField("Company / Organisation")
    email = StringField("Email Address", validators=[DataRequired()])
    phone_number = IntegerField("Phone Number")
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send me a message!")
