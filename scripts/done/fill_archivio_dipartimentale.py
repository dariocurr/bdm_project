from database_connection import database_connection


def creazione_archivio_dipartimentale():
    # dipartimento
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        dipartimenti = list(sql.execute_query("SELECT id_dipartimento, nome FROM dipartimento"))
        for dipartimento in dipartimenti:
            query = "INSERT INTO archivio_dipartimentale(dipartimento) VALUES(" + str(dipartimento[0]) + ")"
            sql.execute_query(query[:-1] + ")")


creazione_archivio_dipartimentale()
