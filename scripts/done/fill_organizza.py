from database_connection import database_connection
import numpy as np


def fill_organizza():
    university = list()
    university.append("unipa")
    university.append("unito")
    university.append("unimi")
    university.append("unina")
    for uni in university:
        #personale_strutturato, evento
        print("INSERIMENTO {}".format(uni))
        sql = database_connection("bdm_{}".format(uni))
        id_personale_strutturato = sql.execute_query("SELECT id_personale_strutturato, ufficio FROM personale_strutturato WHERE 1")
        id_evento = sql.execute_query("SELECT id_evento, argomento FROM evento WHERE 1")
        for evento in id_evento:
            n_rnd = np.random.randint(2, 6)
            for _ in range(1, n_rnd):
                id_personale = np.random.randint(0, len(id_personale_strutturato))
                organizza = (id_personale_strutturato[id_personale][0], evento[0])
                query = "INSERT INTO organizza(personale_strutturato, evento) VALUES ("
                for value in organizza:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")


fill_organizza()
