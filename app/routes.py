from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Austino'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Welcome to Lagos, land of opportunities'
        },
        {
            'author': {'username': 'Cynthia'},
            'body': 'Lagos Bar Beach is the bomb!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
