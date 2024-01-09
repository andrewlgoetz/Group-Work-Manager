from flask import Blueprint
from imports import *

dash_bp = Blueprint("dash_bp", __name__, template_folder='templates', static_folder = 'static')

# Paul handles data for group tasks & their comments, as well as search results
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
    comment_form = GroupTaskCommentForm()
    if comment_form.validate_on_submit():
        # print(comment_form.content.data)
        return paul.post_task_comment_and_redirect(comment_form, id)
    comments = paul.get_task_comments(id)
    task = paul.get_task(id)
    name = paul.get_poster_name(task.poster_id)
    # print(comment_form.errors) # if form not validating

    comment_form.content.data = '' # not entirely neccessary, paul handles this
    return render_template("group_task.html", id=id, comments = comments, task = task, name=name, comment_form=comment_form)


# open a comment
@dash_bp.route("/comment/<int:id>", methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = GroupTaskCommentForm()
    if comment_form.validate_on_submit():
        task_id = paul.get_comment(id).task_id
        return paul.post_threaded_comment_and_redirect(comment_form, id,task_id)
    comments = paul.get_threaded_comments(id)
    parent_comment = paul.get_comment(id)
    name = paul.get_poster_name(parent_comment.poster_id)
    task = paul.get_root_task(id)
    comment_form.content.data = ''
    return render_template("comment.html", id=id, comments=comments, parent_comment=parent_comment, comment_form=comment_form, name=name, task=task)

