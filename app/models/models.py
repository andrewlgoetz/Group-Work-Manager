from imports import *
# from app.extension import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(40), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
	    return '<Name %r>' % self.name


class GroupTasks(db.Model): # TODO reference other users, and each user can see their tasks
    id = db.Column(db.Integer, primary_key=True)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(55))
    content = db.Column(db.Text)
    due_date = db.Column(db.DateTime, default=datetime.utcnow)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, default = 0)
    # actioned_by = db.Column(db.Integer, db.ForeignKey('users.id')) # user working on this task
    tally = db.Column(db.Integer, default = 0)


class GroupTasksComments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey('group_tasks.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('group_tasks_comments.id'), nullable=True, default = 0) # null by default
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # name = db.Column(db.Integer, db.ForeignKey('users.id')) 
    content = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    tally = db.Column(db.Integer, default = 0)

#chart tasks are recurring tasks
class ChartTasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(55))
    content = db.Column(db.Text)
    period = db.Column(db.Integer, default=1)#[1,5]:day, 3 days, week, bi-week, month
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, default = 0)
      
