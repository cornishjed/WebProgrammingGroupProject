#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe
'''
Jozsef-Attila Elec
Group 5
'''

import cgi, string, random,mysql.connector

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='')

form=cgi.FieldStorage()
fromF=form.getvalue('fromFinal')
DestinationF=form.getvalue('toDestFinal')
dateF=form.getvalue('datesFinal')
faresF=form.getvalue('faresFinal')
allPassF=form.getvalue('allPassFinal')
adultsF=form.getvalue('adultsFinal')
childrenF=form.getvalue('childrenFinal')
younglingF=form.getvalue('younglingFinal')
startF=form.getvalue('startFinal')
arrivalF=form.getvalue('arrivalFinal')
payerName=form.getvalue('payName')

def bookingNumber_generator(number,chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars)+random.choice(string.digits) for number in range(3))

bookingNumber = bookingNumber_generator(1,fromF+DestinationF )    

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
		<a href="#" class="nav-bar-item   white">Train</a>
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
print("<h1 class='content-head is-center'> your receipt </h1>")
print('<div class="content-subhead">')
print('<p>Have a great day,',payerName,',thanks for choosing us!</p>')
print('<p>Booking number: ', bookingNumber,'</p>')
print('<br> <p>Your Train leaves from:',fromF,' at ',startF,'and arrives to:',DestinationF,' at ',arrivalF,' on: ', dateF,'</p>')

cursor=conn.cursor()
cursor.execute("INSERT INTO pastbookings (CustomerName , BookingNr ,Froms , Destination , PassengerNR , Date ) VALUES ('%s' , '%s' , '%s' , '%s' , '%s' , '%s');"%(payerName,bookingNumber,fromF,DestinationF,allPassF,dateF))
conn.commit()



 
if(int(adultsF)>0):
    if(int(childrenF)>0):
        if(int(younglingF)>0):
            print(adultsF,'adults,',childrenF,'children and',younglingF,'youngling')
        else:
            print(adultsF,'adults and',childrenF,'children')
    else:
        print(adultsF,'adults and',younglingF,'younglings')
else:
    print(childrenF,'children')
    
print('<p><br> Total price: £',faresF,'</p>')
if(int(adultsF)>0):
    if(int(childrenF)>0):
        if(int(younglingF)>0):
            template="Booking number: {bookingNumber}, Your Train leaves from:{fromF}, at:{startF} and arrives to:{DestinationF} at :{arrivalF}, on:{dateF}, Passengers:{adultsF} adults, {childrenF} children and {younglingF} youngling, Total price: £{faresF}".format(bookingNumber=bookingNumber,fromF=fromF,startF=startF,DestinationF=DestinationF,arrivalF=arrivalF,dateF=dateF,faresF=faresF,adultsF=adultsF,childrenF=childrenF,younglingF=younglingF)
        else:
            template="Booking number: {bookingNumber}, Your Train leaves from:{fromF}, at:{startF} and arrives to:{DestinationF} at :{arrivalF}, on:{dateF}, Passengers:{adultsF} adults and{childrenF} children, Total price: £{faresF}".format(bookingNumber=bookingNumber,fromF=fromF,startF=startF,DestinationF=DestinationF,arrivalF=arrivalF,dateF=dateF,faresF=faresF,adultsF=adultsF,childrenF=childrenF)
    else:
        template="Booking number: {bookingNumber}, Your Train leaves from:{fromF}, at:{startF} and arrives to:{DestinationF} at :{arrivalF}, on:{dateF}, Passengers:{adultsF} adults and {younglingF} youngling, Total price: £{faresF}".format(bookingNumber=bookingNumber,fromF=fromF,startF=startF,DestinationF=DestinationF,arrivalF=arrivalF,dateF=dateF,faresF=faresF,adultsF=adultsF,younglingF=younglingF)
else:
    template="Booking number: {bookingNumber}, Your Train leaves from:{fromF}, at:{startF} and arrives to:{DestinationF} at :{arrivalF}, on:{dateF}, Passengers:{childrenF} children, Total price: £{faresF}".format(bookingNumber=bookingNumber,fromF=fromF,startF=startF,DestinationF=DestinationF,arrivalF=arrivalF,dateF=dateF,faresF=faresF,childrenF=childrenF)
file = open("receipt.txt", "w")
file.write(template)
file.close()

print("<br><h3> Click <a href='http://localhost/webprog/Assignment/group/train/receipt.txt' download>  me </a> to download receipt</h3>")
print('</div>')
print('</div>')
print('</body>')
print('<footer class="footer"> @ Grand Travel Booking - JA 2019 </footer>')
print('</div>')
print('</html>')
