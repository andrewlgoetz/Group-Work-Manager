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


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            # Check the hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Succesfull!!")
                return redirect(url_for('dash_bp.index'))
            else:
                flash("Wrong password.")
        else:
            flash("That User Doesn't Exist! Try Again...")
    
    return render_template('login.html', form=form)
    
    
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for('dash_bp.index'))



@auth_bp.route('/delete_user/<int:id>', methods={'GET', 'POST'})
def delete_user(id):
    if (current_user.id == id or current_user.username == "admin"): #admin profile
        user = Users.query.get_or_404(id)
        print(id)
        print(user.username)
        try:
            db.session.delete(user)
            db.session.commit()
            
            flash("User Deleted")
            existing_users = Users.query.order_by(Users.date_added)
            form = UserForm()
            name = None
            #TODO redirect to new_user, instead of rendering template from this route
            return render_template("new_user.html", form = form, name=name, existing_users=existing_users)
        except:
            flash("Error, user could not be deleted")
            return redirect(url_for('auth_bp.new_user'))
    else:
        abort(403)