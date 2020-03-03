from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from flask_login import login_required, current_user

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos

# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms.fields import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired

app = create_app()

@app.cli.command()
def test():
	tests = unittest.TestLoader().discover('test')
	unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_error(error):
	return render_template('500.html', error=error)

# decorador de python
@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	# response.set_cookie('user_ip', user_ip)
	session['user_ip'] = user_ip
	return response


@app.route('/hello', methods=['GET'])
@login_required
def hello():
	# user_ip = request.cookies.get('user_ip')
	user_ip = session.get('user_ip')
	username = current_user.id
	# username = session.get('username')
	# crear un nuevo diccionario de python
	context = {
		'user_ip': user_ip,
		'todos': get_todos(user_id=username),
		'username': username
	}
	# Expandir variables con ** de python
	return render_template('hello.html', **context)