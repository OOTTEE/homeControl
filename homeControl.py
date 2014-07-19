from flask import Flask, request, make_response, redirect, url_for, render_template
from jinja2 import Environment, PackageLoader
from DB import *
from dataBase import dataBase


app = Flask(__name__)
app.config['DEBUG'] = True
env = Environment(loader=PackageLoader('homeControl', 'templates'))

		
@app.route('/',methods=['GET','POST'])
def homeControl():
	username = request.cookies.get('username')
	if username is not None:
		db = dataBase()
		habitaciones = db.query_db('select * from habitacion')
		db.close_db()
		template = env.get_template('index.html')
		values={ 'pagina' : 'inicio.html',
				 'login' : True,
				 'habitaciones' : habitaciones,
				 'username' : username
		}
	else:
		template = env.get_template('index.html')
		values={ 'login' : False}
	resp = template.render(values)
	return resp
	
@app.route('/login',methods=['GET','POST'])
def login(): 
	db = dataBase()
	rows =  db.query_db(str.format("select * from usuario where name = '{0}' and pass = '{1}'",request.form['username'],request.form['password']))
	db.close_db()
	resp = make_response(redirect('/'))
	if len(rows) == 1:		
		print 'ok'
		resp.set_cookie('username',request.form['username'])
	return resp	
	
@app.route('/habitacion')
def habitacion(): 
	db=dataBase()
	habitaciones = db.query_db('select * from habitacion')
	db.close_db()
	template = env.get_template('index.html')
	values={ 'pagina' : 'habitacion.html',
			 'login' : True,
			 'habitaciones' : habitaciones
	}
	return template.render(values)
	
@app.route('/habitacionAjax',methods=['POST'])
def habitacionAjax(): 
	db=dataBase()
	persianas = db.query_db(str.format("select * FROM componente WHERE fk_h_id = {0}",request.form['id']))
	habitacion = db.query_db(str.format("select name FROM habitacion WHERE h_id = {0}",request.form['id']))
	db.close_db()
	template = env.get_template('habitacion.html')
	values={ 'id' : request.form['id'],
			 'habitacion' : habitacion[0],
			 'persianas' : persianas,
			 'numPersianas': len(persianas)}
	return template.render(values)

@app.route('/addHabitacionAjax',methods=['POST']) 
def addHabitacionAjax():
	db = dataBase()
	db.query_db("INSERT INTO habitacion(name) VALUES (?)",[request.form['name']])
	db.commit_db() 
	db.close_db()
	return 'ok' 
	
	
@app.route('/adminHabitaciones')
def adminHabitacion(): 
	db = dataBase()
	habitaciones = db.query_db('select * from habitacion')
	db.close_db()
	template = env.get_template('index.html')
	values={ 'pagina' : 'adminHabitaciones.html',
			 'login' : True,
			 'habitaciones' : habitaciones
	}
	return template.render(values)
	
@app.route('/adminComponentes')
def adminComponentes(): 
	db = dataBase()
	habitaciones = db.query_db('select * from habitacion')
	db.close_db()
	template = env.get_template('index.html')
	values={ 'pagina' : 'adminComponentes.html',
			 'login' : True, 
	}
	return template.render(values)
	
@app.route('/restartBD')
def restartBD(): 
	print dataBase.init_db()
	return 'ok'
	
if __name__ == '__main__':
	app.run(debug=True)