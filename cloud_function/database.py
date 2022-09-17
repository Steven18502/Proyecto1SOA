import mysql.connector

mydb = mysql.connector.connect(
  host="104.197.57.229",
  user="root",
  password="123456",
  database="Proyecto1"
)
mycursor = mydb.cursor()
sql = "insert into resultados (face, joy, sorrow,anger,surprise) VALUES (%s, %s,%s, %s,%s)"

def insert(val):
  val = (val[0],val[1],val[2],val[3],val[4])
  mycursor.execute(sql, val)
  mydb.commit()
  print("Register inserted!!")