from database_connection import database_connection
import numpy as np
from random import shuffle


def creazione_voce_fondo():
    # nome, descrizione, importo, fondo
    voci = ["attrezzatura", "personale", "eventi", "progetti e ricerca", "manutenzione"]
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        fondi = list(sql.execute_query("SELECT id_fondo, budget FROM fondo"))
        for fondo in fondi:
            sum = round(float(fondo[1]), 2)
            voce_fondo = list()
            shuffle(voci)
            for voce in voci[:-1]:
                importo = round(np.random.uniform(0, sum), 2)
                sum = round(sum - importo, 2)
                voce_fondo.append((voce, "Gettito relativo a " + voce, importo, fondo[0]))
            if sum > 0:
                voce_fondo.append((voci[-1], "Gettito relativo a " + voci[-1], sum, fondo[0]))
            for voce in voce_fondo:
                query = "INSERT INTO voce_fondo(nome, descrizione, importo, fondo) VALUES ("
                for value in voce:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")


creazione_voce_fondo()
