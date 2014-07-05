from flask import Flask
from jinja2 import Environment, PackageLoader
from BD import conn

app = Flask(__name__)
app.config['DEBUG'] = True
env = Environment(loader=PackageLoader('homeControl', 'html'))
		
@app.route('/')
def homeControl():
	c  = conn()
	habitaciones = c.query('select * from habitacion')
	
	#print c.query('insert into habitacion (name) values (\'Salon\')')
	#print c.query('insert into habitacion (name) values (\'Cocina\')')
	#print c.query('insert into habitacion (name) values (\'Viky\')')
	#c.commit()
	c.close()
	template = env.get_template('index.html')
	values={ 'pagina' : 'inicio.html',
			 'login' : True,
			 'habitaciones' : habitaciones
	}
	return template.render(values)
	

@app.route('/login')
def login():
	template = env.get_template('index.html')
	values={ 'login' : False}
	return template.render(values)	
	
@app.route('/habitacion')
def habitacion(): 
	c  = conn()
	habitaciones = c.query('select * from habitacion')
	c.close()
	template = env.get_template('index.html')
	values={ 'pagina' : 'habitacion.html',
			 'login' : True,
			'habitaciones' : habitaciones
	}
	return template.render(values)
	
@app.route('/adminHabitaciones')
def adminHabitacion(): 
	c  = conn()
	habitaciones = c.query('select * from habitacion')
	c.close()
	template = env.get_template('index.html')
	values={ 'pagina' : 'adminHabitaciones.html',
			 'login' : True,
			'habitaciones' : habitaciones
	}
	return template.render(values)
	
@app.route('/adminComponentes')
def adminComponentes(): 
	c  = conn()
	habitaciones = c.query('select * from habitacion')
	c.close()
	template = env.get_template('index.html')
	values={ 'pagina' : 'adminComponentes.html',
			 'login' : True,
	}
	return template.render(values)

if __name__ == '__main__':
	app.run(debug=True)