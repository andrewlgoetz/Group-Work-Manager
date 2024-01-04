from flask import Blueprint
from imports import *


auth_bp = Blueprint("auth_bp", __name__, template_folder='templates', static_folder = 'static')

#login
#logout
#new user
#delete user


@auth_bp.route("/new_user", methods=['GET', 'POST'])
def new_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first() ##if none, then unique username
        if user is None:
            hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
            user = Users(username=form.username.data, name=form.name.data, key=form.key.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()            
        else:
            flash("Username already in use.")
            return redirect(url_for('auth_bp.new_user'))

        name = form.name.data # html
        # clear form
        form.name.data = ''
        form.username.data = ''
        form.key.data = ''
        form.password_hash.data = ''    

    existing_users = Users.query.order_by(Users.date_added)
    return render_template("new_user.html", form = form, name=name, existing_users=existing_users)