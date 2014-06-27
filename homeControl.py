from flask import Flask
app = Flask(__name__)

@app.route('/')
def homeControl():
    return 'Hello World!'
	
@app.route('/prueba/')
def Prueba():
    return 'prueba'

if __name__ == '__main__':
    app.run()