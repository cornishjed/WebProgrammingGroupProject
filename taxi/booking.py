#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe

'''
<!-- /* Name : Dariusz Kwiatkowski */ -->
<!-- /* Student id: 18016079 */ -->
'''
from datetime import datetime
import mysql.connector
import cgi, cgitb



form = cgi.FieldStorage()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="webprog"
    )

departLoc = form.getvalue('From')
arriveLoc = form.getvalue('To')
fname = form.getvalue('fname')
lname = form.getvalue('lname')
email = form.getvalue('email')
adult = form.getvalue('adults')
teen = form.getvalue('teens')
child = form.getvalue('children')
date = form.getvalue('date')

mycursor = mydb.cursor()
mycursor.execute("SELECT Price FROM times_taxi WHERE Start='%s'" % (departLoc))

prices = mycursor.fetchone()[0]

prices2 = prices * int(adult) + prices * int(teen) + prices * int(child) / 2


currentDate = datetime.today().strftime('%Y-%m-%d')




'''

if departLoc == "Aberdeen":
    prices = prices[0] * int(adult)
    total = prices * int(adult)

if departLoc == "Birmingham":
    prices = prices[1]


if departLoc == "Bristol":
    prices = prices[2]

if departLoc == "Cardiff":
    prices = prices[3]
    #childPrices = prices / 2

if departLoc == "Dundee":
    prices = prices[4]

if departLoc == "Edinburgh":
    prices = prices[5]

if departLoc == "Glasgow":
    prices = prices[6]

if departLoc == "Lonodon":
    prices = prices[7]

if departLoc == "Manchester":
    prices = prices[8]

if departLoc == "Newcastle":
    prices = prices[9]

if departLoc == "Portsmouth":
    prices = prices[10]

if departLoc == "Southhampton":
    prices = prices[11]
'''
#childPrices = prices / 2
#total = prices * adult + prices * child


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("<link rel='stylesheet' type='text/css' href='http://localhost/webprog/Assignment/group/taxi/style.css'>")
print("</head>")
print("<body>")
print("<div class='subForm' style='color:white;'>")
print("<h2>Booking Details: </h2>")
print("<h3>Date Booked: %s</h3>" % (currentDate))
print("<h3>Full Name: %s %s</h3>" % (fname, lname))
print("<h3>From: %s</h3>" % (departLoc))
print("<h3>To: %s</h3>" % (arriveLoc))
print("<h3>Date: %s</h3>" % (date))
print("<h3>Adults: %s</h3>" % (adult))
print("<h3>Teens: %s</h3>" % (teen))
print("<h3>Children: %s</h3>" % (child))
print("<h3>Price: £ %d</h3>" % (prices2))
print("</div>")

f = open("payed.txt", "w")
f.write("First Name: %s " % (fname))
f.write("Last Name: %s " % (lname))
f.write("Date Booked: %s " % (currentDate))
f.write("To: %s " % (arriveLoc))
f.write("Date: %s " % (date))
f.write("Adults: %s " % (adult))
f.write("Teens: %s " % (teen))
f.write("Children: %s " % (child))
f.write("Price:£ %s " % (prices2))


f.close()
print("<a href='http://localhost/webprog/Assignment/group/taxi/payed.txt' download>Download receipt</a>")
#print("<h3>Total: %d</h3>" % (int(total)))


print("</body>")
print("</html>")
