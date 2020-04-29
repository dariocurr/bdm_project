import pymysql.cursors

connection = pymysql.connect(host='bdm.zandes.net',
                             port=3306,
                             user='bdm_root',
                             password='progettobdm',
                             db='bdm_uni_riconciliato')


def execute_query(query):
    try:
        with connection.cursor() as sql:
            sql.execute(query)
            result = sql.fetchall()
            if result is not None:
                for row in result:
                    print(row)
            else:
                connection.commit()
    finally:
        connection.close()
