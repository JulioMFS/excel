import sys
import sqlite3
import MySQLdb
import MySQLdb.cursors

#def getEntradaBranha(d):
#===================================================================
# connect to mysql
#===================================================================

try:
    db = MySQLdb.connect(host='https://sanfona.myvnc.com:3306', user='julio', passwd='j301052', db='agro', cursorclass=MySQLdb.cursors.DictCursor)
except MySQLdb.Error as e:
    print ('Error %d: %s' % (e.args[0], e.args[1]))
    sys.exit(1)

#===================================================================
# query select from table
#===================================================================

cursor = db.cursor()

sql = 'SELECT sum(Peso) as sumP FROM `guiaentrada` WHERE Data > "2021-09-01" and GuiaNo between "700" and "799"'

cursor.execute(sql)
recs = cursor.fetchall()
print("Total Rows: ", len(recs))
for row in recs:
    print(row)
    print("peso: ", row["sumP"])
    tot = row["sumP"]
print ('%20s, %10s' % ('Luis Branha', tot))

cursor.close()
db.close()
#    return totPeso
