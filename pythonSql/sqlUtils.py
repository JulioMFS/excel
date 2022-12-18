import MySQLdb
#import mysql.connector
def connectDB():
    connection = MySQLdb.connect(
                    host = 'sanfona.myvnc.com',
                    user = 'julio',
                    passwd = 'j301052')  # create the connection
    return connection
# -----------------------------------------------------------------------------------------------------------
def getTableNames(db):
    conn = connectDB()
    cursor = conn.cursor()
#    db = "agro"
    query = f"USE {db}"
    print(query)
    cursor.execute(query) # select the database

    cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)
    #now there are two options:

    tables = cursor.fetchall()       # return data from last query
    #or iterate over the cursor:
    table = cursor
    #for (table_name,) in cursor:
    #    print(table_name)
    return tables
#-----------------------------------------------------------------------------------------------------------
def getTblColsData():

    conn = connectDB()
    cur = conn.cursor()
    db = "agro"
    query = f"USE {db}"
    cur.execute(query)  # select the database
    try:
        cur.execute("select * from facturas")
        result = cur.fetchall()
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        print(field_names)

        for value in result:
            print(value)

        conn.commit()
    except:
        conn.rollback()
    conn.close()
#-----------------------------------------------------------------------------------------------------------
tables = getTableNames("agro")
# #print(type(tables))
# for item in tables:
#     print(str(item[0]))
# # getTblColsData()