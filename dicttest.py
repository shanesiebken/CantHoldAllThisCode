
##f = open("dict.txt","w")
##f.write( str(dict) )
##f.close()

import sqlite3 as lite
import sys

con = None

con = lite.connect('test.db')
cur = con.cursor()  
cur.execute('SELECT SQLITE_VERSION()')
data = cur.fetchone()
print("SQLite version: %s" % data)
