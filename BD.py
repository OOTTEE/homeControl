import sqlite3
from flask import g, Flask

DATABASE = '/var/www/homeControl/db/dataBase.db'

class conn:
	def __init__(self):
		self.db = getattr(g, '_database', None)
		if self.db is None:
			self.db = g._database = sqlite3.connect(DATABASE)
	
	def close(self):
		self.db = getattr(g, '_database', None)
		if self.db is not None:
			self.db.close()
	
	def query(self,query, args=(), one=False):
		cur = self.db.execute(query,args)
		rv = cur.fetchall()
		cur.close()
		return (rv[0] if rv else None) if one else rv
	
	def commit(self):
		self.db.commit()