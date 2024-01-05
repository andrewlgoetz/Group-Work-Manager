from flask import Blueprint
from imports import *

dash_bp = Blueprint("dash_bp", __name__, template_folder='templates', static_folder = 'static')

# Paul gets data on group tasks & comments
paul = Taskdata()


#index

@dash_bp.route("/", methods=['GET', 'POST'])
def index():
    # task form
    task_form = GroupTaskForm()
    if task_form.validate_on_submit():
        return paul.post_new_task_and_redirect(task_form)
    
    # load group tasks
    tasks = paul.get_homepage_tasks()


    return render_template("index.html", tasks=tasks, task_form=task_form)

#open up a task
@dash_bp.route("/group_task/<int:id>", methods=['GET', 'POST'])
@login_required
def group_task(id):
    comments = paul.get_task_comments(id)
    task = paul.get_task(id)
    comment_form = GroupTaskCommentForm()

    if comment_form.validate_on_submit():
        return paul.post_task_comment_and_redirect(comment_form, id)


    return render_template("group_note.html", id=id, comments = comments, task = task)