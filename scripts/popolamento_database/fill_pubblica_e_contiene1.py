from database_connection import database_connection
import numpy as np


def creazione_pubblica():
    #"bdm_unipa", "bdm_unina", "bdm_unito""
    for db in ["bdm_unimi"]:
        sql = database_connection(db)
        personale_ricerca = list(sql.execute_query("SELECT id_personale_ricerca, anagrafica_personale FROM personale_ricerca"))
        pubblicazione = list(sql.execute_query("SELECT id_pubblicazione FROM pubblicazione"))
        for pubb in pubblicazione:
            personale = list()
            for _ in range(0, np.random.randint(1, 4)):
                persona = personale_ricerca[np.random.randint(0, len(personale_ricerca))]
                if persona not in personale:
                    personale.append(persona)
            for persona in personale:
                dipartimento = str(sql.execute_query("SELECT dipartimento FROM personale WHERE cf =\'" + str(persona[1]) + "\'" ))
                dipartimento = dipartimento[2:dipartimento.find(",")]
                pubblica = (pubb[0], persona[0])
                query = "INSERT INTO pubblica VALUES ("
                for value in pubblica:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")
                contiene = (int(dipartimento), pubb[0])
                query = "INSERT INTO contiene_1 VALUES ("
                for value in contiene:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")


creazione_pubblica()
