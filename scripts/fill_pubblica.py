from database_connection import database_connection
import numpy as np


def creazione_pubblica():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        personale_ricerca = list(sql.execute_query("SELECT id_personale_ricerca, tipologia_contratto FROM personale_ricerca"))
        pubblicazione = list(sql.execute_query("SELECT id_pubblicazione FROM pubblicazione"))
        for pubb in pubblicazione:
            personale = list()
            for _ in range(0, np.random.randint(1, 4)):
                persona = personale_ricerca[np.random.randint(0, len(personale_ricerca))][0]
                if persona not in personale:
                    personale.append(persona)
            for persona in personale:
                pubblica = (persona, pubb[0])
                print(pubblica)
                """
                query = "INSERT INTO pubblica VALUES ("
                for value in pubblica:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")
                """


creazione_pubblica()
