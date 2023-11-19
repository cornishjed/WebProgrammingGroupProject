#! C:\Users\Student\AppData\Local\Programs\Python\Python37\python.exe
'''
Jozsef-Attila Elec
Group 5
'''

import cgi

form=cgi.FieldStorage()
fromP=form.getvalue('fromPayment')
Destination=form.getvalue('toDestPayment')
dateP=form.getvalue('datesPayment')
faresP=form.getvalue('faresPayment')
allPassP=form.getvalue('allPassPayment')
adultsP=form.getvalue('adultsPayment')
childrenP=form.getvalue('childrenPayment')
younglingP=form.getvalue('younglingPayment')
startP=form.getvalue('startPayment')
arrivalP=form.getvalue('arrivalPayment')


print('''Content-type: text/html\n\n
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="CSSFile.css">
<link rel="stylesheet" href="w3.css"> 
<title> Grand Travel Booking </title>
<script>
function paymentValidation(){
var cardPattern=/^4[0-9]{12}(?:[0-9]{3})?$/;
var postalPattern=/^"GIR[ ]?0AA|((AB|AL|B|BA|BB|BD|BH|BL|BN|BR|BS|BT|CA|CB|CF|CH|CM|CO|CR|CT|CV|CW|DA|DD|DE|DG|DH|DL|DN|DT|DY|E|EC|EH|EN|EX|FK|FY|G|GL|GY|GU|HA|HD|HG|HP|HR|HS|HU|HX|IG|IM|IP|IV|JE|KA|KT|KW|KY|L|LA|LD|LE|LL|LN|LS|LU|M|ME|MK|ML|N|NE|NG|NN|NP|NR|NW|OL|OX|PA|PE|PH|PL|PO|PR|RG|RH|RM|S|SA|SE|SG|SK|SL|SM|SN|SO|SP|SR|SS|ST|SW|SY|TA|TD|TF|TN|TQ|TR|TS|TW|UB|W|WA|WC|WD|WF|WN|WR|WS|WV|YO|ZE)(\d[\dA-Z]?[]?\d[ABD-HJLN-UW-Z]{2}))|BFPO[ ]?\d{1,4}"/;
var name=document.getElementById('name').value;
var card=document.getElementById('cardNumber').value;
var expiryD=document.getElementById('expiry').value;
var cvv=document.getElementById('cvv').value;
var postal=document.getElementById('postal').value;
var cardResult=cardPattern.test(card);
var postalResult=postalPattern.test(postal);

if(name === ""){
alert("Please enter a name");
}
else if(!isNaN(name)){
alert("Enter a valid name!");
}
else if(card===""|| expiryD===""|| cvv===""){

alert("Please fill in you card info");
    if(!cardResult)
    {
    alert("Enter valid card format!");
    }
    }
else if(postal===""){
alert("Enter your postal code!");
}
else if(!postalResult)
{
    alert("Enter a valid postcode!");
}
   
    



}
</script>
</head>''') # javascript
print('<body>')
print('''div class="splash-container">
			<div class="top-bar ">
				<div class="nav-bar">
    
					<a href="#" class="nav-bar-item button-hvr ">Home</a>
					<a href="#" class="nav-bar-item   button-hvr">Planes</a>
					<a href="#" class="nav-bar-item   white">Train</a>
					<a href="#" class="nav-bar-item	  button-hvr">Taxi</a>
    
				</div>
			</div>
''')
print('<img src="http://localhost/webprog/Assignment/group/train/images/train-homepage.jpg" alt="train" class="home-img">')

print('''<div class="content-wrapper" style="top:300px;">
			<div class="content">
''')
print('<div class="is-center"')
print('<h1>Payment Invoice</h1>')
print('<form action="receipt.py" method="get">')
print('Payment amount : ', faresP)
print('<br>')
print('Name on card')
print('<input type="text" id="name" name="payName" placeholder="First Name Last Name">')
print('<br>')
print('Card number')
print('<input type="text" id="cardNumber" name="cardNumber" maxlength="16" placeholder="4114 1234 5678 9101">')
print('<br>')
print('Expiry date')
print('<input type="month" id="expiry" name="cardExp">')
print('<br>')
print('CVV')
print('<input type="text" id="cvv" size="3" name="CVV" maxlength="3" placeholder="123">') 
print('Postal Code')
print('<input type="text" size=8 id="postal" name="postalCode">')
print('<h1> hello </h1>')
#passing values
print("<input type='hidden' name='fromFinal' value='%s'>"%fromP)
print("<input type='hidden' name='toDestFinal' value='%s'>"%Destination)
print("<input type='hidden' name='datesFinal' value='%s'>"%dateP)
print("<input type='hidden' name='faresFinal' value='%s'>"%faresP)
print("<input type='hidden' name='allPassFinal' value='%s'>"%allPassP)
print("<input type='hidden' name='adultsFinal' value='%s'>"%adultsP)
print("<input type='hidden' name='childrenFinal' value='%s'>"%childrenP)
print("<input type='hidden' name='younglingFinal' value='%s'>"%younglingP)
print("<input type='hidden' name='startFinal' value='%s'>"%startP)
print("<input type='hidden' name='arrivalFinal' value='%s'>"%arrivalP)
print('<input type="submit" value="Pay" onmouseover="paymentValidation()">')
print('</form>')
print('</body>')
print('</div>')
print('<footer class="footer"> @ Grand Travel Booking - JA 2019 </footer>')
print('</div>')
print('</html>')
