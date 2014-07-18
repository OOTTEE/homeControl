from flask import Flask, request, make_response, redirect, url_for
from jinja2 import Environment, PackageLoader
from DB import *


app = Flask(__name__)
app.config['DEBUG'] = True
env = Environment(loader=PackageLoader('homeControl', 'templates'))

		
@app.route('/',methods=['GET','POST'])
def homeControl():
	username = request.cookies.get('username')
	if username is None:
		habitaciones = query_db('select * from habitacion')
		close_db(None)
		template = env.get_template('index.html')
		values={ 'pagina' : 'inicio.html',
				 'login' : True,
				 'habitaciones' : habitaciones,
				 'username' : username
		}
	else:
		template = env.get_template('index.html')
		values={ 'login' : False}
	return template.render(values)
	
@app.route('/login',methods=['GET','POST'])
def login(): 
	print request.form['username']
	print request.form['password']
	return redirect('/')	
	
@app.route('/habitacion')
def habitacion(): 
	db=get_db()
	habitaciones = query_db('select * from habitacion')
	close_db(None)
	template = env.get_template('index.html')
	values={ 'pagina' : 'habitacion.html',
			 'login' : True,
			'habitaciones' : habitaciones
	}
	return template.render(values)
	
@app.route('/adminHabitaciones')
def adminHabitacion(): 
	db=get_db()
	habitaciones = query_db('select * from habitacion')
	close_db(None)
	template = env.get_template('index.html')
	values={ 'pagina' : 'adminHabitaciones.html',
			 'login' : True,
			'habitaciones' : habitaciones
	}
	return template.render(values)
	
@app.route('/adminComponentes')
def adminComponentes(): 
	db=get_db()
	habitaciones = query_db('select * from habitacion')
	close_db(None)
	template = env.get_template('index.html')
	values={ 'pagina' : 'adminComponentes.html',
			 'login' : True,
	}
	return template.render(values)
	
@app.route('/restartBD')
def restartBD(): 
	get_db()
	init_db()
	return 'ok'

if __name__ == '__main__':
	app.run(debug=True)