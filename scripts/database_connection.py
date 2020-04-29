import pymysql.cursors

connection = pymysql.connect(host='bdm.zandes.net',
                             port=3306,
                             user='bdm_root',
                             password='progettobdm',
                             db='bdm_uni_riconciliato')


def execute_query(query):
    try:
        with connection.cursor() as sql:
            # Read a single record
            sql.execute(query)
            result = sql.fetchone()
            if result is not None:
                print(result)
            else:
                connection.commit()
    finally:
        connection.close()
