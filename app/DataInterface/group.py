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