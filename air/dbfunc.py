#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe
import cgi, cgitb, mysql.connector, imp

# MYSQL CONFIG VARIABLES
host           = "localhost";
db             = "webprog";
user           = "root";
passwd         = ""

def getConnection():
	conn = mysql.connector.connect(user=user,
								   password=passwd,
								   host=host,
								   database=db)
	return conn
