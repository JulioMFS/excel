import sys

import MySQLdb
import MySQLdb.cursors

#===================================================================
# connect to mysql
#===================================================================

try:
    db = MySQLdb.connect(host='sanfona.myvnc.com', user='julio', passwd='j301052', db='agro', cursorclass=MySQLdb.cursors.DictCursor)
except MySQLdb.Error as e:
    print ('Error %d: %s' % (e.args[0], e.args[1]))
    sys.exit(1)

#===================================================================
# query select from table
#===================================================================

cursor = db.cursor()

#sql = 'SELECT Data, GuiaNo, SUM(Peso) AS totalsize, COUNT(*) AS filecount FROM guiaentrada GROUP BY Data ORDER BY Data DESC;'
sql = "select * from facturas where Date > '2022-09-01' and Fornecedor = 'Agromais'"

cursor.execute(sql)
all_rows = cursor.fetchall()

print (len(all_rows)) # How many rows are returned.
field_names = [i[0] for i in cursor.description]
print(field_names)
print(field_names[1], field_names[2], field_names[4], field_names[7], field_names[10], field_names[13], field_names[14])
for row in all_rows: # While loops always make me shudder!
    d = row['Date'].strftime("%Y-%m-%d")
    print ('%s %s %s %.2f %.2f %s %s' % (d, row['InvNo'], row['Designacao'], row['Preco'], row['ValorLiq'], row['Fornecedor'], row['Parcela']))
#    print(row)

cursor.close()
db.close()