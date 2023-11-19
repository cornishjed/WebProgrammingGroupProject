#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe

# Jed Powell - Group 5

import cgi, cgitb, dbfunc, mysql.connector, datetime, random
from datetime import datetime

template = '''<!DOCTYPE html>
<html>
<title>Grand Travel Booking - Great deals to popular UK destinations</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="w3.css">
<script type="text/javascript" src="https://cdn.jsdelivr.net/jquery/latest/jquery.min.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/momentjs/latest/moment.min.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/daterangepicker/daterangepicker.min.js"></script>
<body>
<!-- Navbar -->
<div class="w3-display-container">
  <div class="w3-bar w3-black w3-card w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="http://localhost/webprog/Assignment/group/index.html" class="w3-bar-item w3-button w3-padding-large w3-hover-white">Home</a>
    <a href="http://localhost/webprog/Assignment/group/air/indexair.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-white">Plane</a>
    <a href="http://localhost/webprog/Assignment/group/train/HomePage.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-grey">Train</a>
    <a href="http://localhost/webprog/Assignment/group/taxi/index.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-grey">Taxi</a>
  </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">
    <a href="http://localhost/webprog/Assignment/group/" class="w3-bar-item w3-button w3-padding-large">Home</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Plane</a>
    <a href="http://localhost/webprog/Assignment/group/train/HomePage.html" class="w3-bar-item w3-button w3-padding-large">Train</a>
    <a href="http://localhost/webprog/Assignment/group/taxi/index.html" class="w3-bar-item w3-button w3-padding-large">Taxi</a>
  </div>
</div>
<div class="w3-display-container" style="margin-bottom:50px">
  <img src="http://localhost/webprog/Assignment/group/air/images/london.jpg" alt="logo and london" style="width:100%">
</div>'''

#cgitb.enable() 
#cgi.test() to test cgi
conn = dbfunc.getConnection()

now = datetime.now()
currentdate = now.strftime("%d/%m/%Y, %H:%M:%S")

form = cgi.FieldStorage()
fname = form.getvalue('fname')
lname = form.getvalue('lname')
phone = form.getvalue('phone')
email = form.getvalue('email')
fromCity = form.getvalue('fromCity')
toCity = form.getvalue('toCity')
adult = int(form.getvalue('adult'))
childl = int(form.getvalue('childl'))
childs = int(form.getvalue('childs'))
date = form.getvalue('usrdate')
fare = int(form.getvalue('fare'))
deptTime = form.getvalue('deptTime')
arrTime = form.getvalue('arrTime')
totalFare = form.getvalue('totalFare')
seats = adult + childl + childs
totalchild = childl + childs

if conn.is_connected():
  cursor = conn.cursor()
  cursor.execute("INSERT INTO seats (departing_from,arriving_to,date,seatno) VALUES('%s','%s','%s','%s')"%(fromCity,toCity,date,seats)) # %s being placeholders
  conn.commit()    
  cursor.close()

conn.close()

childFare = fare/2

bookingID = random.randint(1,10000001)
bookingID = date + str(bookingID)

fhbookingID = "Booking ID: " + bookingID + "\n"
fhcurrentdate = "Date of purchase: " + currentdate + "\n"
fhfname = "First Name: " + fname + "\n"
fhlname = "Last Name: " + lname + "\n"
fhphone = "Phone: " + phone + "\n"
fhdateFlight = "Journey Date: " + date + "\n"
fhfromCity = "Departing from: " + fromCity + "\n"
fhdeptTime = "Time of departure: " + deptTime + "\n"
fhtoCity = "Arriving at: " + toCity + "\n"
fharrTime = "Time of arrival: " + arrTime + "\n"
fhadult = "No. of adults: " + str(adult) + "\n"
fhchild = "No. of children: " + str(totalchild) + "\n"
fhtotalFare = "Total amount payable: £" + str(totalFare) + "\n"

fh = open('receipt.txt', 'w')
fh.write("------------------------------------GRAND TRAVEL BOOKING: RECEIPT-----------------------------------\n")
fh.write("Grand Travel Booking - Thank you for booking and see you again soon..\n")
fh.write("Receipt for ")
fh.write(fhbookingID)
fh.write("------------------------------------CUSTOMER DETAILS-----------------------------------\n")
fh.write(fhfname)
fh.write(fhlname)
fh.write(fhphone)
fh.write("------------------------------------JOURNEY DETAILS-----------------------------------\n")
fh.write(fhdateFlight)
fh.write(fhfromCity)
fh.write(fhdeptTime)
fh.write(fhtoCity)
fh.write(fharrTime)
fh.write(fhadult)
fh.write(fhchild)
fh.write("\n")
fh.write(fhcurrentdate)
fh.write(fhtotalFare)
fh.close()



print('Content-type: text/html \n')
print(template)
print("<div class='w3-row w3-container' style='margin:50px 0'>")
print("<div class='w3-half w3-container'>")
print("<h2>Thank you for booking with us! Here is your printable receipt. Please show this upon boarding and pay your fare upon arrival.</h2>")
if (totalchild > 0):
    print("<img src='http://localhost/webprog/Assignment/group/air/images/family.jpg' alt='family' style='width:100%'/>")
else:
    print("<img src='http://localhost/webprog/Assignment/group/air/images/business.jpg' alt='office' style='width:100%'/>")
print("<br><p>To download a printable receipt, please click <a href='http://localhost/webprog/Assignment/group/air/receipt.txt' download>here</a>")
print("</div>")
print("<div class='w3-half w3-container'>")
print("<h1>Booking Confirmation and Receipt</h1><hr>")
print("<h4>First Name: ", fname, "</h4>")
print("<h4>Surname: ", lname, "</h4>")
print("<h4>Phone: ", phone, "</h4>")
print("<h4>Departing from: ", fromCity, "</h4>")
print("<h4>Time of departure: ", deptTime, "</h4>")
print("<h4>Arriving at: ", toCity, "</h4>")
print("<h4>Time of arrival: ", arrTime, "</h4>")
print("<h4>Fare per person: &pound;", fare, "</h4>")
print("<h4>No. of adults: ", adult, "</h4>")
if (totalchild > 0):
    print("<h4>No. of children: ", totalchild, "</h4>")
    print("<h4>Fare per child under 10: &pound;", childFare, "</h4>")
print("<h4>Total amount payable: &pound;", totalFare, "</h4>")
print("<br>")
print("<h4>Booking ID: ", bookingID, "</h4>")
print("</div>")
print("<div class='w3-display-container' style='margin-bottom:50px'>")
print("<div class='w3-half w3-container'>")
print("<footer>")
print("<p style=font-size:17px>&copy; <em>Grand Travel Booking 2019</em></p>")
print("</footer>")
print("</div>")
print("</div>")
print("</body>")
print("</html>")



conn.close()

