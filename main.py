from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['TODO 1', 'TODO 2', 'TODO 3']

# decorador de python
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    # crear un nuevo diccionario de python
    context = {
    	'user_ip': user_ip,
    	'todos': todos
    }
    # Expandir variables con ** de python
    return render_template('hello.html', **context)
