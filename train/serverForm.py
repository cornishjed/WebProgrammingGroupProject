#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe

'''
Jozsef-Attila Elec
Group 5
'''


import cgi, cgitb, mysql.connector, datetime

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='')

from1= " "
form = cgi.FieldStorage()
from1 = form.getvalue('From')
dates= form.getvalue('date')

adults = int(form.getvalue("adults"))
children = int(form.getvalue("children"))
youngling = int(form.getvalue("younglings"))



to1 = form.getvalue('To1')
to2 = form.getvalue('To2')
to3 = form.getvalue('To3')
to4 = form.getvalue('To4')
to5 = form.getvalue('To5')
to6 = form.getvalue('To6')
to7 = form.getvalue('To7')
to8 = form.getvalue('To8')
to9 = form.getvalue('To9')
to10 = form.getvalue('To10')
toDest= ""

if (from1 == "Aberdeen"):
    toDest = to1
elif (from1 == "Birmingham"):
    toDest = to2
elif (from1 == "Bristol"):
    toDest = to3
elif (from1 == "Cardiff"):
    toDest = to4
elif (from1 == "Dundee"):
    toDest = to5
elif (from1 == "Glasgow"):
    toDest = to6
elif (from1 == "London"):
    toDest = to7
elif (from1 == "Manchester"):
    toDest = to8
elif (from1 == "Newcastle"):
    toDest = to9
elif (from1 == "Southampton"):
    toDest = to10


start= " "
arrival= " "

fares=0
cursor = conn.cursor()
cursor.execute("SELECT WebTrain FROM fares WHERE FromST='%s' AND Destination='%s'"% (from1,toDest))
fares=int(cursor.fetchall()[0][0])
#you got to get the first value of the column [0][0]
cursor.execute("SELECT Start FROM times_train WHERE Leaves ='%s'"% from1)
start= int(cursor.fetchall()[0][0].seconds)
start = datetime.timedelta(seconds=start)
#You get more queries you have t ostore them.
#cursor.execute("SELECT End FROM times_train WHERE Leaves ='Bristol' ;")


cursor.execute("SELECT End FROM times_train WHERE Arrives='%s'"% toDest)
#cursor.execute("SELECT End FROM times_train WHERE Arrives='Edinburgh'")
 #this is the right WAY! 
arrival=int(cursor.fetchall()[0][0].seconds)#converting the tuple to int seconds
arrival=datetime.timedelta(seconds=arrival)#converting seconds to hours,minutes and seconds.


    
discount= fares / 1/2
allPassenger = 0
allPassenger = int(adults) + int(children) + int(youngling)
#allPassenger = str(adults) + str(children) + str(youngling)
#fares= fares * (adults+children+youngling) 
if (youngling >= 1):
    if(children >= 1):
        fares= (fares * (adults+children))+ (discount * youngling)
    else:
        fares = (fares * (adults)) + (discount + youngling)
elif(children >= 1):
    fares = fares * (adults+children)
else:
    fares=fares * (adults)

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
print('<h2 class="content-head is-center"> Summary</h2>')
cursor.execute("SELECT sum(PassengerNR) FROM pastbookings WHERE Date='%s' AND Destination='%s' GROUP BY DATE;"%(dates,toDest))
row=cursor.fetchone()
if row is not None:
    passengerAmount=int(cursor.fetchall()[0])
else:
    passengerAmount=1
#passengerAmount=301  #hypothetical to check
if(passengerAmount < 300): # check if seats are left
    #have the if statement here
    print('<form action="payment.py" method="get">')
    print('<p> From is %s</p>' % from1)
    print('<p> To is %s</p><br>' % toDest)
    print('<p> The journey date is: ', dates,' Leaves ', from1,' at: ', start , ' arrives to: ', toDest,' at: ', arrival,'<br> </p>')
    print('<p> Number of passengers : ',allPassenger  , ' of which adults: ', adults ,', children: ' , children ,' and younglings: ',youngling , ' </p>')
    print('<hr><p> The total price: £', fares,'</p>')
    print("<input type='hidden' name='fromPayment' value='%s'>"%from1)
    print("<input type='hidden' name='toDestPayment' value='%s'>"%toDest)
    print("<input type='hidden' name='datesPayment' value='%s'>"%dates)
    print("<input type='hidden' name='faresPayment' value='%s'>"%fares)
    print("<input type='hidden' name='allPassPayment' value='%s'>"%allPassenger)
    print("<input type='hidden' name='adultsPayment' value='%s'>"%adults)
    print("<input type='hidden' name='childrenPayment' value='%s'>"%children)
    print("<input type='hidden' name='younglingPayment' value='%s'>"%youngling)
    print("<input type='hidden' name='startPayment' value='%s'>"%start)
    print("<input type='hidden' name='arrivalPayment' value='%s'>"%arrival)
    print('<br> Do you wish to procceed with your Booking?')
    print('<br><a href="http://localhost/webprog/Assignment/group/train/HomePage.html"><input type="button" value="No"> </a>')
    print('<input type="submit" value="Yes">')
    print('</form>')
    print('</div>')
    print('</body>')
    print('<footer class="footer"> @ Grand Travel Booking - JA 2019 </footer>')
    print('</div>')
    print('</html>')

else:
    print('<br> <h2> NO MORE SEATS LEFT ON SELECTED JOURNEY <h2> <br>')
    print('<a href="http://localhost/webprog/Assignment/group/train/HomePage.html"><input type="button" value="GO BACK"> </a>')
    print('</div>')
    print('</body>')
    print('<footer class="footer"> @ Grand Travel Booking - JA 2019 </footer>')
    print('</div>')
    print('</html>')
