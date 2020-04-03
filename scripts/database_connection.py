import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='',
                             db='database_bdm')


def execute_query(query):
    try:
        with connection.cursor() as sql:
            # Read a single record
            sql.execute(query)
            result = sql.fetchone()
            print(result)
    finally:
        connection.close()


execute_query("SELECT * FROM `personale`")
