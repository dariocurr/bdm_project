import pymysql.cursors

connection = pymysql.connect(host='localhost',port=3306,user='root',password='',db='test');

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `name` FROM `test`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
