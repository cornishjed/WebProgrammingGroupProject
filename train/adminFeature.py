#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe
'''
Jozsef-Attila Elec
Group 5
'''

import cgi

print('content-type: text/html \n')
print('<html>')
print('<head>')
print('<title> ADMIN Booking </title>')
print('<link rel="stylesheet" href="http://localhost/webprog/Assignment/group/train/CSSFile.css">')
print('<link rel="stylesheet" href="http://localhost/webprog/Assignment/group/train/w3.css">')
print('<h1> Welcome Admin </h1>')
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
print('<div class="splash">')
print('<h1 class="splash-head"> Administrator</h1>')
print('<h1 class="splash-subhead"> maintenance</h1>')
print('</div>')
print('</div>')
print('<div class="content-wrapper">')
print('<div class="content">')
print('<p> Hello</p>')
print('<p> type what yo uwould like to do</p><br>')
choice=input('<input type="text">')

print('<p> your choice is ',choice,'<p>')
print('</div>')
print('</div>')
