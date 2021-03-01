import mysql.connector

""" ydb = mysql.connector.connect(
  host="3.133.13.224",
  user="nperic",
  password="AS3@394$57w*21QSvxa",
  database="project") */"""

import mysql.connector

try:
    connection = mysql.connector.connect(host="3.133.13.224",
                                        user="nperic",
                                        password="AS3@394$57w*21QSvxa",
                                        database="project")

    query = """CREATE TABLE bpm ( 
                             Id int(11) NOT NULL,
                             Id int(11) NOT NULL) """

    cursor = connection.cursor()
    result = cursor.execute(query)
    print("table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

