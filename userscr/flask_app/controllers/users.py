from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def user_dashboard():
    users = user.User.get_all_users()
    print(users)
    return render_template('users_dashboard.html', all_users=users)

@app.route('/users/<int:id>')
def show_user(id):
    data={
        'id': id
    }
    focus=user.User.get_one_user(data)
    print(focus)
    return render_template('show_user.html',user=focus)


@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    user.User.save_user(data)
    return redirect('/users')

@app.route('/users/<int:id>/edit')
def editing_user(id):
    data={
        'id':id
    }
    focus=user.User.get_one_user(data)
    return(render_template('edit_user.html',user=focus))

@app.route('/edit/submit', methods=['POST'])
def edit_user():
    user.User.edit_user(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def remove_user(id):
    data={
        'id':id
    }
    user.User.delete_user(data)
    return redirect('/users')