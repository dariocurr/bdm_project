from database_connection import database_connection
import numpy as np


def creazione_finanzia3():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        voce_spesa = list(sql.execute_query("SELECT id_voce_spesa, nome FROM voce_spesa WHERE nome = \'progetto ricerca\'"))
        progetti_ricerca = list(sql.execute_query("SELECT id_progetto, nome FROM progetto_ricerca"))
        for voce in voce_spesa:
            progetto = progetti_ricerca[np.random.randint(0, len(progetti_ricerca))]
            finanzia = (voce[0], progetto[0])
            query = "INSERT INTO finanzia_3 VALUES ("
            for value in finanzia:
                query += "'" + str(value) + "',"
            sql.execute_query(query[:-1] + ")")


creazione_finanzia3()
