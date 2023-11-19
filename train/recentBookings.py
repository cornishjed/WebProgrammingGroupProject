#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe
'''
Jozsef-Attila Elec
Group 5
'''


import cgi,mysql.connector

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='')

form=cgi.FieldStorage()
cursor=conn.cursor()
customerName=form.getvalue('nameCustomer')

cursor.execute("SELECT * FROM pastbookings WHERE CustomerName='%s'"%customerName)
customerInfo=str(cursor.fetchall()[0])

print('content-type: text/html \n')
print('<html>')
print('<head>')
print('<title> Grand Travel Booking </title>')
print('<link rel="stylesheet" href="http://localhost/webprog/Assignment/group/train/CSSFile.css">')
print('<link rel="stylesheet" href="http://localhost/webprog/Assignment/group/train/w3.css">')
print('</head>')
print('<body>')
print('<div class="splash-container">')
print('''<div class="top-bar ">
	    <div class="nav-bar">
    
		<a href="http://localhost/webprog/Assignment/group/index.html" class="nav-bar-item button-hvr ">Home</a>
		<a href="http://localhost/webprog/Assignment/group/air/indexair.html" class="nav-bar-item   button-hvr">Planes</a>
		<a href="http://localhost/webprog/Assignment/group/train/HomePage.html" class="nav-bar-item   white">Train</a>
		<a href="http://localhost/webprog/Assignment/group/taxi/index.html" class="nav-bar-item	  button-hvr">Taxi</a>
    
	    </div>
	</div>''')
print('<img src="http://localhost/webprog/Assignment/group/train/images/train-homepage.jpg" alt="train" class="home-img">')
print('<div class="splash">')
print('<h1 class="splash-head"> grand travel booking</h1>')
print('<h1 class="splash-subhead"> Booking Summarry</h1>')
print('</div>')
print('</div>')
print('<div class="content-wrapper">')
print('<div class="content">')
print("<h1 class='content-head is-center'> your recent bookings </h1>")
print('<div class="content-subhead">')
print('<h2> Name--BkngNr---From---To---PsngrNR---Date----  <h2>')
print('<h2>',customerInfo,'</h2>')
