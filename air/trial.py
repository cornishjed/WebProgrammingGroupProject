import cgi, cgitb, dbfunc, mysql.connector, datetime


conn = dbfunc.getConnection()

if conn.is_connected():
   #print('Connected to MySQL database')
   check = conn.cursor()
   check.execute("SELECT seatno FROM seats WHERE date = '%s' AND departing_from = '%s' AND arriving_to = '%s'"%(date,fromCity,toCity))
   seattaken = int(cursor.fetchone()[0][0])
   print(seattaken)
  #cursor = conn.cursor()
  #cursor.execute("INSERT INTO seats (departing_from,arriving_to,date,seats) VALUES('%s','%s','%s','%s')"%(fromCity, toCity, date, seats)) # %s being placeholders  

  #conn.commit()    
#cursor.close()
