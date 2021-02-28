import mysql.connector

mydb = mysql.connector.connect(
  host="3.133.13.224",
  user="nperic",
  password="AS3@394$57w*21QSvxa",
  database="project"
)

mycursor = mydb.cursor()


sql = "INSERT INTO heartbeats (totalHeartBeats, height, gender) VALUES (%s, %s, %s)"
val = (50, "5'10", "Male")
mycursor.execute(sql, val)


mydb.commit()

print(mycursor.rowcount, "record inserted.")