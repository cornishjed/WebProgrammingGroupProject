function formValidation() {
    let city1 = document.getElementById("fromCity").value;
    let city2 = document.getElementById("toCity").value;

    let destinations = {
        Aberdeen: ['Portsmouth'],
        Birmingham: ['Newcastle'],
        Bristol: ['Newcastle', 'Manchester', 'London', 'Glasgow'],
        Cardiff: ['Edinburgh'],
        Dundee: ['Portsmouth'],
        Edinburgh: ['Cardiff'],
        Glasgow: ['Newcastle'],
        London: ['Manchester'],
        Manchester: ['Bristol', 'Glasgow', 'Southampton'],
        Newcastle: ['Bristol', 'Manchester', 'Birmingham'],
        Portsmouth: ['Dundee'],
        Southhampton: ['Manchester']
    }
    
    if (city1 === city2) {
        document.getElementById("dest").innerHTML = "Cannot book flight from/to same city";
        return false;
    }
    else if (city1 === 'Aberdeen' && !destinations.Aberdeen.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Portsmouth only.";
        return false;
    }
    else if (city1 === 'Birmingham' && !destinations.Birmingham.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Newcastle only.";
        return false;
    }
    else if (city1 === 'Bristol' && !destinations.Bristol.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Newcastle, Manchester, London and Glasgow only.";
        return false;
    }
    else if (city1 === 'Cardiff' && !destinations.Aberdeen.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Edinburgh only.";
        return false;
    }
    else if (city1 === 'Dundee' && !destinations.Dundee.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Portsmouth only.";
        return false;
    }
    else if ((city1 == 'Edinburgh') && !destinations.Edinburgh.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Bristol, Manchester and Birmingham only.";
        return false;
    }
    else if (city1 === 'Glasgow' && !destinations.Glasgow.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Newcastle only.";
        return false;
    }
    else if (city1 === 'London' && !destinations.London.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Manchester only.";
        return false;
    }
    else if ((city1 == 'Manchester') && !destinations.Manchester.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Bristol, Glasgow and Southampton only.";
        return false;
    }
    else if ((city1 == 'Newcastle') && !destinations.Newcastle.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Bristol, Manchester and Birmingham only.";
        return false;
    }
    else if (city1 === 'Portsmouth' && !destinations.Portsmouth.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Dundee.";
        return false;
    }
    else if (city1 === 'Southampton' && !destinations.Southhampton.includes(city2)) {
        document.getElementById("dest").innerHTML = "To Manchester only.";
        return false;
    }
     else {
        document.getElementById("dest").innerHTML = "";
    }			

    let userdate = document.getElementById("usrdate").value;
    let adult = document.getElementById("adult").value;
    let childl = document.getElementById("childl").value;
    let childs = document.getElementById("childs").value;
    
    if (!userdate)
    {
        //alert ('Date must be specified');
        document.getElementById("when").innerHTML = "Date must be specified";
        return false;
    }
    
    else
    {
        document.getElementById("when").innerHTML = "";
    }
    
    
    if((adult == 0) && (childs >= 1))
    {
        document.getElementById("msg").innerHTML = "Children under 10 must be accompanied by an adult";
        return false;
    }
    else
    {
        document.getElementById("msg").innerHTML = "";
    }
    
    if((adult == 0) && (childl == 0))
    {
        //alert ('At least 1 passenger please');
        document.getElementById("msg").innerHTML = "At least 1 passenger please";
        return false;
    }
    else if((adult == 0) && (childl > 0))
    {
        document.getElementById("msg").innerHTML = "";
    }
    else
    {
        document.getElementById("msg").innerHTML = "";
    }
    
    
    userDate = new Date(userdate);

   // alert ("User Date " + userDate);

    CurrentDate = new Date();
    //alert ("Current Date " + CurrentDate);

    let day = userDate.getDay();
    
    if (day == 6 || day == 0)
    {
        //alert ('Flights Mon-Fri only');
        document.getElementById("when").innerHTML = "Flights Mon-Fri only";
        document.MyForm.usrdate.focus();
        document.getElementById("usrdate").style.border='1px solid red';
        return false;
    }
    else if (userDate < CurrentDate)
    {
        //alert ('Please select a date from today');
        document.getElementById("when").innerHTML = "Please select a date from today";
        document.MyForm.usrdate.focus();
        document.getElementById("usrdate").style.border='1px solid red';
        return false;
    }
    else
    {
        document.getElementById("when").innerHTML = "";
    }
    
   // alert(userDate - CurrentDate); // returns milliseconds 

    //Check number of months between current date and user date
    let difference = userDate.getMonth() - CurrentDate.getMonth();

    if (difference > 3)
    {
        //alert ('Only 3 months advance booking is allowed');
        document.getElementById("when").innerHTML = "Only 3 months advance booking is allowed";
        document.MyForm.usrdate.focus();
        document.getElementById("usrdate").style.border='1px solid red';
        return false;

    }
    else
    {
        //document.getElementById("temp").innerHTML = "Date is validated";
        //alert('Date is validated')
        document.getElementById("dest").innerHTML = "";
        return true;          
    }
        
}