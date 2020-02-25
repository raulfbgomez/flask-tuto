from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)

# app.config['SECRET_KEY'] = 'super secreto'
app.config.from_pyfile('config.py')

todos = ['TODO 1', 'TODO 2', 'TODO 3']

class LoginForm(FlaskForm):
	# e validator unicamente agrega un required de HTML
	username = StringField('nombre de usuario', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Enviar')

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


@app.route('/hello')
def hello():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    # formulario
    login_form = LoginForm()
    # crear un nuevo diccionario de python
    context = {
    	'user_ip': user_ip,
    	'todos': todos,
    	'login_form': login_form
    }
    # Expandir variables con ** de python
    return render_template('hello.html', **context)
