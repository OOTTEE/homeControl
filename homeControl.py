from flask import Flask
from jinja2 import Environment, PackageLoader
app = Flask(__name__)
env = Environment(loader=PackageLoader('homeControl', 'html'))
		
@app.route('/')
def homeControl():
	template = env.get_template('index.html')
	return template.render(pagina='inicio.html')
	
	
@app.route('/habitacion')
def habitacion(): 
	template = env.get_template('index.html')
	return template.render(pagina='habitacion.html')
	
@app.route('/adminHabitaciones')
def adminHabitacion(): 
	template = env.get_template('index.html')
	return template.render(pagina='adminHabitaciones.html')
	
@app.route('/adminComponentes')
def adminComponentes(): 
	template = env.get_template('index.html')
	return template.render(pagina='adminComponentes.html')

	

if __name__ == '__main__':
	app.run()