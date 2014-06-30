from flask import Flask
from jinja2 import Environment, PackageLoader
app = Flask(__name__)
env = Environment(loader=PackageLoader('homeControl', 'html'))
		
@app.route('/')
def homeControl():
	template = env.get_template('index.html')
	template = env.get_template('habitacion.html')
	return template.render()
	
	
@app.route('/prueba/')
def Prueba(): 
    return 'prueba'

if __name__ == '__main__':
	app.run()