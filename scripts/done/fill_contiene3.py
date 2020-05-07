from database_connection import database_connection
import numpy as np


def creazione_contiene3():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        dipartimenti = list(sql.execute_query("SELECT id_dipartimento, nome FROM dipartimento"))
        progetti_ricerca = list(sql.execute_query("SELECT id_progetto, nome FROM progetto_ricerca"))
        for progetto in progetti_ricerca:
            dipartimenti_aggiunti = list()
            for _ in range(0, np.random.randint(1, 5)):
                dipartimento = dipartimenti[np.random.randint(0, len(dipartimenti))][0]
                if dipartimenti not in dipartimenti_aggiunti:
                    dipartimenti_aggiunti.append(dipartimento)
            for dipartimento in dipartimenti_aggiunti:
                contiene = (dipartimento, progetto[0])
                query = "INSERT INTO contiene_3 VALUES ("
                for value in contiene:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")


creazione_contiene3()
