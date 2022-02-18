from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from video.models import Videos


class Register(FlaskForm):
    #video_name = StringField('Video Name', validators=[DataRequired(), validate_videoname(), Length(min=2, max=20)])
    video_file = FileField('Upload Video',)
    submit = SubmitField('Upload')

    def validate_videoname(self, username):
        video = Videos.query.filter_by(video_name=video_name.data).first()
        if video:
            raise ValidationError('This video name is taken. Please choose a different one.')


