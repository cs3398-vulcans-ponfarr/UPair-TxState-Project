from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    school = SelectField(u'School', choices=[(228459, 'Texas State University'), (229115, 'Texas Tech University')], coerce=int)
    #username = StringField('Username',
    #                       validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    student_id = StringField('Student ID', validators=[Regexp(r'^[\w]+$'), Length(min=1, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ScheduleForm(FlaskForm):
    major = SelectField('Major', coerce=int)
    course = SelectField('Class', coerce=int)

