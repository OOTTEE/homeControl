from flask import Flask, request, make_response, redirect, url_for, render_template, session
from jinja2 import Environment, PackageLoader
from dataBase import dataBase


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = '\x07\x05\x86}\x15\x03\xc2\xee\xb7]\xd9l\x92\x17\xe80WqM\xe9e$\xdfK'
env = Environment(loader=PackageLoader('homeControl', 'templates'))

'''
	Ruta principal de la pagina, verifica si el usuario esta logueado.
'''	
@app.route('/',methods=['GET','POST'])
def homeControl(): 
	if 'username' in session:
		db = dataBase()
		habitaciones = db.query_db('select * from habitacion')
		db.close_db()
		template = env.get_template('index.html')
		values={ 'pagina' : 'inicio.html',
				 'login' : True,
				 'habitaciones' : habitaciones,
				 'username' : session['username']
		}
	else:
		template = env.get_template('index.html')
		values={ 'login' : False}
	return template.render(values)
	
'''
	Pagina de login se comprueba si el usuario se ha logueado correctamente
'''
@app.route('/login',methods=['POST'])
def login(): 
	db = dataBase()
	rows =  db.query_db(str.format("select * from usuario where name = '{0}' and pass = '{1}'",request.form['username'],request.form['password']))
	db.close_db()
	if len(rows) == 1:
		session['username'] = request.form['username']
	return make_response(redirect('/'))	
'''
	Pagina de salida, se redirecciona a la pagina de login
'''
@app.route('/logout') 
def logout():
	session.pop('username', None)
	return redirect('/')
	
'''
	recupera la vista de la pagina principal
'''
@app.route('/inicio',methods=['POST'])
def inicio(): 
	if 'username' in session:
		db = dataBase()
		habitaciones = db.query_db('select * from habitacion')
		db.close_db()
		template = env.get_template('inicio.html')
		values={ 'habitaciones' : habitaciones,
				 'username' : session['username']
		}
		return template.render(values) 
	else:
		return 'not-login'

'''
	Ser recupera la vista de la pagina de habitaciones
'''
@app.route('/habitacion',methods=['POST'])
def habitacion(): 
	if 'username' in session:
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
	else:
		return 'not-login'		
		
'''
	Anhade una habitacion a la BD
'''
@app.route('/addHabitacion',methods=['POST']) 
def addHabitacion():
	if 'username' in session:
		db = dataBase()
		db.query_db("INSERT INTO habitacion(name) VALUES (?)",[request.form['name']])
		db.commit_db() 
		db.close_db()
		return redirect('/adminHabitaciones') 
	else:
		return 'not-login'
		
@app.route('/adminHabitaciones',methods=['POST','GET'])
def adminHabitacion(): 
	if 'username' in session:
		db = dataBase()
		habitaciones = db.query_db('select * from habitacion')
		db.close_db()
		template = env.get_template('adminHabitaciones.html')
		values={ 'habitaciones' : habitaciones
		}
		return template.render(values)
	else:
		return 'not-login'		
		
'''
	Pagina de administracion de componentes
'''
@app.route('/adminComponentes',methods=['GET','POST'])
def adminComponentes(): 
	db = dataBase()
	habitaciones = db.query_db('select * from habitacion')
	db.close_db()
	template = env.get_template('index.html')
	values={ 'pagina' : 'adminComponentes.html',
			 'login' : True, 
	}
	return template.render(values)
'''
	pagina para la restauracion de la base de datos
'''
@app.route('/restartBD')
def restartBD(): 
	dataBase.init_db() 
	return 'ok'
	
if __name__ == '__main__':
	app.run(debug=True)