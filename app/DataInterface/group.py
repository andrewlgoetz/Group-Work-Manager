from imports import *
## ^^ data base already imported

class Taskdata():
    def __init__(self):
        pass
    
    def get_homepage_tasks(self):
        tasks = GroupTasks.query.order_by(GroupTasks.date_posted)
        get_tasks = []
        for i in tasks:
            get_tasks.append(i)
        return get_tasks[::-1]

    def post_new_task_and_redirect(self, form):
        task = GroupTasks(title = form.title.data, content = form.content.data, poster_id = current_user.id) 
        form.title.data = ''
        form.content.data = ''
        db.session.add(task)
        db.session.commit()
        flash("Task Posted")
        return redirect(url_for("dash_bp.index"))

    def post_task_comment_and_redirect(self, form, task_id):
        comment = GroupTasksComments(task_id = task_id, poster_id=current_user.id, content = form.content.data)
        # print(form.content.data)
        # print("x")
        form.content.data = ''
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("dash_bp.group_task", id=task_id))

    def post_threaded_comment_and_redirect(self, form, parent_id):
        comment = GroupTasksCommentsThreaded(parent_id=parent_id, poster_id=current_user.id, content=form.content.data)
        form.content.data = ''
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("dash_bp.comment", id = parent_id))
    
    def post_threaded_comment_and_redirect_to_threaded(self, form, parent_id):
        comment = GroupTasksCommentsThreaded(parent_id=parent_id, poster_id=current_user.id, content=form.content.data)
        form.content.data = ''
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("dash_bp.threaded_comment", id = parent_id))

    def get_threaded_comments(self, parent_id):
        parent_comment = GroupTasksComments.query.get_or_404(parent_id)
        child_comments = []
        get_comments = GroupTasksCommentsThreaded.query.filter_by(parent_id = parent_id)
        for i in get_comments:
            child_comments.append(i)
        return child_comments      

    ## TODO def search for root task of a comment

    def get_comment(self, id):
        return GroupTasksComments.query.get_or_404(id)
    
    def get_parent_comment(self, id):
        return GroupTasksCommentsThreaded.query.get_or_404(id)

    def get_task_comments(self, id):
        task = GroupTasks.query.get_or_404(id)
        comments = []
        get_comments = GroupTasksComments.query.filter_by(task_id = id)
        for i in get_comments:
            comments.append(i)
        return comments

    def get_poster_name(self, poster_id ):
        return Users.query.filter_by(id = poster_id).first().name

    def get_task(self, id):
        return GroupTasks.query.get_or_404(id)


