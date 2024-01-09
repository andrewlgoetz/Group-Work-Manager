from flask import Blueprint
from imports import *


search_bp = Blueprint("search_bp", __name__, template_folder='templates', static_folder = 'static')


paul = Taskdata()




@search_bp.route("/search", methods=['POST'])
@login_required
def search():
    form = SearchForm()
    tasks = GroupTasks.query
    if form.validate_on_submit():
        searched = form.searched.data
        tasks= tasks.filter((GroupTasks.content.like("%" + searched + "%"))).all()
        return render_template("search.html", form=form, searched=searched, tasks=tasks)




