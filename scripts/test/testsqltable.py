import mysql.connector

mydb = mysql.connector.connect(
  host="3.133.13.224",
  user="nperic",
  password="AS3@394$57w*21QSvxa",
  database="project"
)

mycursor = mydb.cursor()


sql = "SELECT * FROM heartbeats;"
mycursor.execute(sql)
records = mycursor.fetchall()
print('Total number of rows in table', mycursor.rowcount)

for row in records:
    print(row[0])
    print(row[1])
    print(row[2])


mydb.commit()

print(mycursor.rowcount, "record inserted.")