import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='',
                             db='database_bdm')

try:
    with connection.cursor() as sql:
        # Read a single record
        query = "SELECT * FROM `personale`"
        sql.execute(query)
        result = sql.fetchone()
        print(result)
finally:
    connection.close()
