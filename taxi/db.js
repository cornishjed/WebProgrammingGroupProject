function optionChange()
{
  var a ="Aberdeen";
  var bi = "Birmingham";
  var br = "Bristol";
  var c = "Cardiff";
  var d = "Dundee";
  var e = "Edinburgh";
  var g = "Glasgow";
  var l = "Lonodon";
  var m = "Manchester";
  var n = "Newcastle";
  var p = "Portsmouth";
  var s = "Southhampton";
  var test = document.getElementById("From");
  var select = document.getElementById("To");

  if(test.selectedIndex == "0")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(p);
  }

  if(test.selectedIndex == "1")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(n);

  }

  if(test.selectedIndex == "2")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(n);
      select.options[select.options.length] = new Option(m);
      select.options[select.options.length] = new Option(l);
  }

  if(test.selectedIndex == "3")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(e);
  }

  if(test.selectedIndex == "4")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(p);
  }

  if(test.selectedIndex == "5")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(c);
  }

  if(test.selectedIndex == "6")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(n);
  }

  if(test.selectedIndex == "7")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(m);
  }

  if(test.selectedIndex == "8")
  {
      select.options.length = 0;
      select.options[select.options.length] = new Option(br);
      select.options[select.options.length] = new Option(g);
      select.options[select.options.length] = new Option(s);
  }

  if(test.selectedIndex == "9")
  {
    select.options.length = 0;
    select.options[select.options.length] = new Option(br);
    select.options[select.options.length] = new Option(m);
    select.options[select.options.length] = new Option(bi);
  }

  if(test.selectedIndex == "10")
  {
    select.options.length = 0;
    select.options[select.options.length] = new Option(d);
  }

  if(test.selectedIndex == "11")
  {
    select.options.length = 0;
    select.options[select.options.length] = new Option(m);
  }
}


function validation()
{
  adult = document.getElementById('adult').value;
  child = document.getElementById('child').value;
  date = document.getElementById('date').value;


  if(adult == 0 && child > 0)
  {
    alert("Children under 12 cannot travel without an adult.");
    document.getElementById("finalCheck").addEventListener("click", function(event){
  event.preventDefault()
});
  }
}
