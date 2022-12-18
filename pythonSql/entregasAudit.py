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
#mycursor.execute("SHOW tables")

#for x in mycursor:
#  print(x)
#mycursor.execute("select * from guiaentrada Where Data > '2022-09-01' LIMIT 2")
mycursor.execute("select Parcela, Data, Hora, PesoVerde, ConvTN, PesoVerde * ConvTN, Peso, (PesoVerde * ConvTN) - Peso"
                 "  from guiaentrada Where Data > '2022-09-01'"
                 "   and Parcela = 'Praia'"
                 " order by Parcela, Data, Hora")

columns = mycursor.description
result = [{columns[index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]

#pprint.pprint(result)

#===================================================================
# query select from table
#===================================================================

cursor = mydb.cursor()

sql = "select Parcela, Data, Hora, PesoVerde, ConvTN, PesoVerde * ConvTN as pesoCalc," \
    " Peso, (PesoVerde * ConvTN) - Peso as Diff"  \
    "  from guiaentrada Where Data > '2022-09-01'"  \
    " order by Parcela, Data, Hora"

cursor.execute(sql)
all_rows = cursor.fetchall()
colnames = cursor.description
print((colnames[0][0]), "\t", colnames[1][0], "\t\t\t", colnames[2][0], "\t\t", colnames[3][0], "\t", colnames[4][0], "\t", colnames[5][0], "\t", colnames[6][0], "\t\t", colnames[7][0])
for column in cursor:
    print(column[0], "\t", column[1], "\t", column[2], "\t", column[3], "\t", column[4], "\t", column[5], "\t", column[6], "\t", column[7])
print(len(all_rows)) # How many rows are returned.

cursor.close()
mydb.close()