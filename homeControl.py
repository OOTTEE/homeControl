from flask import Flask
from jinja2 import Environment, PackageLoader
app = Flask(__name__)
env = Environment(loader=PackageLoader('homeControl', 'html'))
		
@app.route('/')
def homeControl():
	template = env.get_template('index.html')
	return template.render(the='variables', go='here')
	
	
@app.route('/prueba/')
def Prueba(): 
    return 'prueba'

if __name__ == '__main__':
	app.run(debug=True)