from database_connection import database_connection


id_uni = 1
offset = 0
for db in ["bdm_unipa", "bdm_unimi", "bdm_unito", "bdm_unina"]:
    sql = database_connection(db)
    tables = list(sql.execute_query("SHOW TABLES"))
    sql.close_connection()
    for table in tables:
        sql = database_connection(db)
        sql_uni = database_connection("bdm_uni_riconciliato")
        keys = list(sql.execute_query("DESCRIBE " + str(table[0])))
        rows = list(sql.execute_query("SELECT * FROM " + str(table[0])))
        for row in rows:
            row = list(row)
            index = 0
            for value in row:
                if (keys[index][3] == "MUL" or keys[index][3] == "PRI"):
                    if keys[index][0] != "cf" and keys[index][0] != "anagrafica_personale":
                        row[index] += offset
                index += 1
            if table[0] == "dipartimento":
                row = row + [id_uni]
            query = "INSERT INTO " + table[0] + " VALUES ("
            for value in row:
                if isinstance(value, str):
                    value = value.lower()
                query += "'" + str(value) + "',"
            sql_uni.execute_query(query[:-1] + ")")
        print("caricata tabella " + table[0])
        sql_uni.close_connection()
        sql.close_connection()
    offset += 100000
    id_uni += 1
    print("caricato db " + db)
