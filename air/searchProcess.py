#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe

# Jed Powell - Group 5

import cgi, cgitb, dbfunc, mysql.connector, datetime

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
    <a href="" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-white">Plane</a>
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

form = cgi.FieldStorage()
keys = list(form.keys())
fromCity = form.getvalue('fromCity')
toCity = form.getvalue('toCity')
adult = int(form.getvalue('adult'))
childl = int(form.getvalue('childl'))
childs = int(form.getvalue('childs'))
date = form.getvalue('usrdate')

print('Content-type: text/html \n')
print(template)


if conn.is_connected():
   #print('Connected to MySQL database')
   cursor = conn.cursor()
   cursor.execute("SELECT SUM(seatno) FROM seats WHERE departing_from = '%s' AND arriving_to =  '%s' AND date = '%s'"%(fromCity,toCity,date))
   row = cursor.fetchone()
   if row[0] is None:
      seats = 0
   else:
      seats = int(row[0])
   #seats=61
   #print(seats)
   if (seats <= 60):
      date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y/%m/%d')
      cursor = conn.cursor()
      cursor.execute("SELECT fare FROM webair WHERE departing_from = '%s' AND arriving_at = '%s'"%(fromCity,toCity))
      fare = int(cursor.fetchone()[0])
      cursor.execute("SELECT departure_time FROM webair WHERE departing_from = '%s' AND arriving_at = '%s'"%(fromCity,toCity))
      deptTime = cursor.fetchone()[0]
      cursor.execute("SELECT arrival_time FROM webair WHERE departing_from = '%s' AND arriving_at = '%s'"%(fromCity,toCity))
      arrTime = cursor.fetchone()[0]
      adultFare = int(fare * (adult + childl))
      childFare = int((fare / 2) * childs)
      totalFare = adultFare + childFare
      print("<div class='w3-row w3-container' style='margin:50px 0'>")
      print("<h1 align='center'>Your Booking Results</h1>")
      print("<hr>")
      print("<h2>From: ", fromCity, "<br>To: ", toCity, "</h2>")
      print("<table border=1 align='center'>")
      print("<tr><td><h3>Price per ticket</h3></td><td><h4>&pound;",fare,"</h4></td></tr>")
      print("<tr><td><h3>Date of travel</h3></td><td><h4>", date, "</h4></td></tr>")
      print("<tr><td><h3>Departure Time</h3></td><td><h4>", deptTime, "</h4></td></tr>")
      print("<tr><td><h3>Arrival Time</h3></td><td><h4>", arrTime, "</h4></td></tr>")
      print("<tr><td><h3>Total Fare</h3></td><td><h4>&pound;", totalFare, "</h4></td></tr>")
      print("</table>")
      print("<p>*all times displayed in Greenwich Mean Time (GMT)</p>")
      print("<hr><p>To continue booking this journey, please fill in the form below and click submit to confirm booking. To return to the previous page, please click <a href=http://localhost/webprog/Assignment/group/air/indexair.html>here</a></p>")
      print("<br><form action='reciept.py' method='POST' name='MyForm'>")
      print("<h5>First Name: <input type='text' name='fname' id='fname'/></h5>")
      print("<h5>Last Name: <input type='text' name='lname' id='lname'/></h5>")
      print("<h5>Telephone: <input type='number' name='phone' id='phone'/></h5>")
      print("<h5>Email: <input type='email' name='email' id='email'/></h5>")
      print("<input type='hidden' name='fromCity' value='%s'>"%fromCity)
      print("<input type='hidden' name='toCity' value='%s'>"%toCity)
      print("<input type='hidden' name='usrdate' value='%s'>"%date)
      print("<input type='hidden' name='adult' value='%s'>"%adult)
      print("<input type='hidden' name='childl' value='%s'>"%childl)
      print("<input type='hidden' name='childs' value='%s'>"%childs)
      print("<input type='hidden' name='fare' value='%d'>"%fare)
      print("<input type='hidden' name='deptTime' value='%s'>"%deptTime)
      print("<input type='hidden' name='arrTime' value='%s'>"%arrTime)
      print("<input type='hidden' name='totalFare' value='%d'>"%totalFare)
      print("<input class='w3-btn w3-black' type='submit' value='Book journey'>")
      print("</form>")
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
   else:
      print("<p>Not enough seats</p>")
      print("<a href='http://localhost/webprog/Assignment/group/air/indexair.html'>Click here to return</a>")
      print("<div class='w3-display-container' style='margin-bottom:50px'>")
      print("<div class='w3-half w3-container'>")
      print("<footer>")
      print("<p style=font-size:17px>&copy; <em>Grand Travel Booking 2019</em></p>")
      print("</footer>")
      print("</div>")
      print("</div>")
      print("</body>")
      print("</html>")

   

   cursor.close()
conn.close()
