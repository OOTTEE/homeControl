import sqlite3

DATABASE = '/var/www/homeControl/db/database.db'
SCHEMA = '/var/www/homeControl/db/db.sql'

class dataBase:
	def __init__(self):
		self.conn = sqlite3.connect(DATABASE)
		self.c = self.conn.cursor()

	def query_db(self, query, args=()):
		if len(args) > 1:
			return self.c.executemany(query, args).fetchall()
		else:
			return self.c.execute(query, args).fetchall()
	
	def commit_db(self):
		self.conn.commit()

	def close_db(self):
		self.conn.close()
	
	@staticmethod
	def init_db():
		conn = sqlite3.connect(DATABASE)
		f = open(SCHEMA,'r')
		conn.cursor().executescript(f.read())
		conn.commit()
		conn.close()

