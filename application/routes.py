from application import app
from flask import render_template

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
