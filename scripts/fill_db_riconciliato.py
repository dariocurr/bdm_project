from database_connection import database_connection


sql_uni = database_connection("bdm_uni_riconciliato")
id_uni = 1
offset = 0
for db in ["bdm_unipa", "bdm_unimi", "bdm_unito", "bdm_unina"]:
    db += "_backup"
    sql = database_connection(db)
    tables = list(sql.execute_query("SHOW TABLES"))
    for table in tables:
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
            if table[0] == "contiene_3":
                query = "INSERT INTO " + table[0] + " VALUES ("
                for value in row:
                    query += "'" + str(value) + "',"
                sql_uni.execute_query(query[:-1] + ")")
        print("caricata tabella " + table[0])
    offset += 100000
    id_uni += 1
    print("caricato db " + db)
