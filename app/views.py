from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')

def index():
	user = {'nickname': 'Keith'}
	posts = [
		{
			'author': {'nickname': 'John'},
			'body': "Fuckoff!",
		},
		{
			'author': {'nickname': 'Bill'},
			'body': 'I like things!'
		}
	 ]
	return render_template('index.html',
						   title = 'Home',
						   user = user,
						   posts = posts)

def index():
	user = {'nickname': 'Keith'}
	posts = [
		{
			'author': {'nickname': 'John'},
			'body': "Fuckoff!",
		},
		{
			'author': {'nickname': 'Bill'},
			'body': 'I like things!'
		}
	 ]
	return render_template('index.html',
						   title = 'Home',
						   user = user,
						   posts = posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
						   title='Sign In',
						   form=form)

