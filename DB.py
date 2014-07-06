import sqlite3
from flask import g, Flask

app = Flask(__name__)
app.config['DEBUG'] = True

DATABASE = '/var/www/homeControl/db/database.db'
SCHEMA = '/var/www/homeControl/db/db.sql'

def get_db():
	db = getattr(g,'_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
		print 'conectando'
	return db


@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
	cur = get_db().execute(query,args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

			
def commit_db():
	db = getattr(g, '_database', None)
	if db is None:
		db.commit()

def init_db():
	with app.app_context():
		c = conn()
		db = c.get_db()
		with app.open_resource(SCHEMA, mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()
		
@app.teardown_appcontext
def close_db():
		db = getattr(g, '_database', None)
		if db is not None:
			db.close()
