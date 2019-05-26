from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from my_blog.models import User


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("login")


class RegistrationForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     EqualTo('pass_confirm', message="passwords_must_match")])
    pass_confirm = PasswordField("Confirmed pass", validators=[DataRequired()])
    submit = SubmitField("Register")


    def check_email(self, field):
        if User.query.filter_by(email=field.email.data).first():
            raise ValidationError("This email is already used!")

    def check_username(self, field):
        if User.query.filter_by(username=field.email.data).first():
            raise ValidationError("This username is already used!")


class UpdateUserForm(FlaskForm):

    email = StringField("Email: ", validators=[DataRequired(), Email()])
    username = StringField("Username: ", validators=[DataRequired()])
    picture = FileField('Update profile pictue', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def check_email(self, field):
        if User.query.filter_by(email=field.email.data).first():
            raise ValidationError("This email is already used!")

    def check_username(self, field):
        if User.query.filter_by(username=field.email.data).first():
            raise ValidationError("This username is already used!")

