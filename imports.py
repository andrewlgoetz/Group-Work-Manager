from flask import Flask, render_template,  g,  flash, request, redirect, url_for, session, abort
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField,  BooleanField, ValidationError, TextAreaField, HiddenField
from wtforms.validators import DataRequired, EqualTo, length
from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import date
# from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm, SearchForm
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm
from flask_ckeditor import CKEditor
from werkzeug.utils import secure_filename
import uuid as uuid
import sqlite3
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField


#forms
from app.forms import UserForm as UserForm
from app.forms import LoginForm as LoginForm
from app.forms import GroupTaskForm as GroupTaskForm
from app.forms import GroupTaskCommentForm as GroupTaskCommentForm
from app.forms import SearchForm as SearchForm
# from app.forms import GroupTaskThreadedCommentForm as GroupTaskThreadedCommentForm

## Models
from app.extension import db as db
from app.models.models import Users as Users
from app.models.models import GroupTasks as GroupTasks
from app.models.models import GroupTasksComments as GroupTasksComments
# from app.models.models import GroupTasksCommentsThreaded as GroupTasksCommentsThreaded


# Data Interface
from app.DataInterface.group import Taskdata as Taskdata