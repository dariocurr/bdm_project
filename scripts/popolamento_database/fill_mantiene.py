from database_connection import database_connection
import numpy as np


def creazione_mantiene():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        personale_ricerca = list(sql.execute_query("SELECT id_personale_ricerca, tipologia_contratto FROM personale_ricerca"))
        attivita_didattica = list(sql.execute_query("SELECT id_attivita_didattica, nome FROM attivita_didattica"))
        for attivita in attivita_didattica:
            professori = list()
            for _ in range(0, np.random.randint(1, 4)):
                prof = personale_ricerca[np.random.randint(0, len(personale_ricerca))][0]
                if prof not in professori:
                    professori.append(prof)
            ruolo = ["professore", "professore", "assistente"]
            for prof in professori:
                mantiene = (prof, attivita[0], ruolo[np.random.randint(0, 3)], np.random.randint(2000, 2020))
                query = "INSERT INTO mantiene VALUES ("
                for value in mantiene:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")


creazione_mantiene()
