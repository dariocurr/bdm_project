from database_connection import database_connection
import numpy as np


def creazione_finanzia2():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        voce_spesa = list(sql.execute_query("SELECT id_voce_spesa, nome FROM voce_spesa WHERE nome = \'evento\'"))
        eventi = list(sql.execute_query("SELECT id_evento, data FROM evento"))
        for voce in voce_spesa:
            evento = eventi[np.random.randint(0, len(eventi))]
            finanzia = (voce[0], evento[0])
            query = "INSERT INTO finanzia_2 VALUES ("
            for value in finanzia:
                query += "'" + str(value) + "',"
            sql.execute_query(query[:-1] + ")")


creazione_finanzia2()
