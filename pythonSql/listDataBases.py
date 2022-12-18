import pprint
import MySQLdb

import MySQLdb as mysql

mydb = mysql.connect(
  host="sanfona.myvnc.com",
  user="julio",
  password="j301052",
  database="agro"
)

mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES")
mycursor.execute("SHOW tables")

for x in mycursor:
  print(x)
mycursor.execute("select * from guiaentrada Where Data > '2021-10-01' LIMIT 2")
columns = mycursor.description
result = [{columns[index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]

pprint.pprint(result)