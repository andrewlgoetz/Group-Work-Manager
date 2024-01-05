from imports import *

# Users
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()]) #TODO add email validator
    key = StringField("key", validators=[DataRequired()]) # lkhf6oy4
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords do not match.')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Group Tasks
class GroupTaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField("Submit")

#Comments
class GroupTaskCommentForm(FlaskForm):
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField("Submit")

class GroupTaskThreadedCommentForm(FlaskForm):
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField("Submit")