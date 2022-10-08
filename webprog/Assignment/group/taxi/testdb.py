#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe


'''
<!-- /* Name : Dariusz Kwiatkowski */ -->
<!-- /* Student id: 18016079 */ -->
'''

import mysql.connector
import cgi, cgitb

form = cgi.FieldStorage()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="webprog"
    )

mycursor = mydb.cursor()
mycursor.execute("SELECT Price FROM times_taxi ORDER BY Start")

prices = mycursor.fetchall()




print("Content-type:text/html\r\n\r\n")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='http://localhost/webprog/Assignment/group/taxi/style.css'>")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("</head>")
# c and t acts as indexes that itarate the list by one
c = 0
t = 0
print("<body>")
print("<div class='bookingForm'>")
print("<form id='formBook' action='booking.py' method='POST'>")
print("<h3>First Name:</h3>")
print("<input type='text' name='fname' required><br>")
print("<h3>Surname:</h3>")
print("<input type='text' name='lname' required><br>")
print("<h3>Email:</h3>")
print("<input type='email' name='email' required><br>")
print("<h3>From:</h3>")
print("<select name='From' id='From' onchange='optionChange();'>")
print("<option hidden disabled selected value>Select an option</option>")
print("<option value='Aberdeen'>Aberdeen</option>")
print("<option value='Birmingham'>Birmingham</option>")
print("<option value='Bristol'>Bristol</option>")
print("<option value='Cardiff'>Cardiff</option>")
print("<option value='Dundee'>Dundee</option>")
print("<option value='Edinburgh'>Edinburgh</option>")
print("<option value='Glasgow'>Glasgow</option>")
print("<option value='Lonodon'>Lonodon</option>")
print("<option value='Manchester'>Manchester</option>")
print("<option value='Newcastle'>Newcastle</option>")
print("<option value='Portsmouth'>Portsmouth</option>")
print("<option value='Southhampton'>Southhampton</option>")

#for i in myresult:
  #print("<option value=>%s</option>" % (myresultFrom[c]))
 # c = c + 1

print("</select>")
print("<br><br>")
print("<h3>To:</h3>")
#print("<select  id='To'>")
print("<select name='To' id='To'>")
print("<option hidden></option>")
print("<option value='Aberdeen'>Aberdeen</option>")
print("<option value='Birmingham'>Birmingham</option>")
print("<option value='Bristol'>Bristol</option>")
print("<option value='Cardiff'>Cardiff</option>")
print("<option value='Dundee'>Dundee</option>")
print("<option value='Edinburgh'>Edinburgh</option>")
print("<option value='Glasgow'>Glasgow</option>")
print("<option value='Lonodon'>Lonodon</option>")
print("<option value='Manchester'>Manchester</option>")
print("<option value='Newcastle'>Newcastle</option>")
print("<option value='Portsmouth'>Portsmouth</option>")
print("<option value='Southhampton'>Southhampton</option>")

#for i in myresult:
 # print("<option value=>%s</option>" % (myresultTo[t]))
  #t = t + 1


print("</select>")
print("<br><br>")
print("<h3>Date:</h3>")
print("<input type='date' id='date' name='date' required><br>")
print("<h3>Adults (16+):</h3>")
print("<input type='number' min='0' placeholder='e.g. 1' id='adult' name='adults'><br>")
print("<h3>Children (<12-16):</h3>")
print("<input type='number' min='0' placeholder='e.g. 1' id='teen' name='teens'><br>")
print("<h3>Chidlren (under 10):</h3>")
print("<div id='childDiv'>")
print("<input type='number' min='0' placeholder='e.g. 1' id='child' name='children'><br><br>")
print("</div>")
print("<button class='submitButton' type='submit' id='finalCheck' value='submit' onclick='validation()'>Previewbutton")
print("</form>")
print("</div>")
print("<script src='http://localhost/webprog/Assignment/group/taxi/db.js'></script>")
print("</body>")
