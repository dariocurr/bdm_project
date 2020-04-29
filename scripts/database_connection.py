import pymysql.cursors


class database_connection():

    def __init__(self, database):
        self._connection = pymysql.connect(host='bdm.zandes.net',
                                           port=3306,
                                           user='bdm_root',
                                           password='progettobdm',
                                           db=database)

    def execute_query(self, query):
        with self._connection.cursor() as sql:
            sql.execute(query)
            result = sql.fetchall()
            self._connection.commit()
            return result
