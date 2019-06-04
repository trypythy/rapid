from application import app
from flask import render_template, flash, redirect, url_for
from application.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Buster'}
	reviews = [
        {
            'author': {'username': 'Jaya'},
            'body': 'Beautiful day in Philadelphia!'
        },
        {
            'author': {'username': 'Buster'},
            'body': 'this is going to be a ride for sure'
        }
    ]
	return render_template('index.html', title='Home', user=user, reviews=reviews)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html',title='Sign in', form=form)
