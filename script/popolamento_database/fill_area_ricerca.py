from database_connection import database_connection


def creazioni_aree_ricerca():
    # nome, descrizione
    area_ricerca = list()
    area_ricerca.append(("Biologia", ""))
    area_ricerca.append(("Bioinformatica", ""))
    area_ricerca.append(("Medicina", ""))
    area_ricerca.append(("Matematica", ""))
    area_ricerca.append(("Fisica", ""))
    area_ricerca.append(("Farmacia", ""))
    area_ricerca.append(("Ingegneria", ""))
    area_ricerca.append(("Architettura", ""))
    area_ricerca.append(("Economia", ""))
    area_ricerca.append(("Psicologia", ""))
    area_ricerca.append(("Scienze del mare", ""))
    area_ricerca.append(("Turismo", ""))
    area_ricerca.append(("Informatica", ""))
    sql = database_connection("bdm_unipa")
    for area in area_ricerca:
        query = "INSERT INTO area_ricerca(nome, descrizione) VALUES ("
        for value in area:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    sql = database_connection("bdm_unimi")
    for area in area_ricerca:
        query = "INSERT INTO area_ricerca(nome, descrizione) VALUES ("
        for value in area:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    sql = database_connection("bdm_unina")
    for area in area_ricerca:
        query = "INSERT INTO area_ricerca(nome, descrizione) VALUES ("
        for value in area:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    sql = database_connection("bdm_unito")
    for area in area_ricerca:
        query = "INSERT INTO area_ricerca(nome, descrizione) VALUES ("
        for value in area:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")


creazioni_aree_ricerca()
