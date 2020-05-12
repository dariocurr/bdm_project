import random
from database_connection import database_connection


def creazione_finanzia_1():
    for db in  ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        personale_strutturato = list(sql.execute_query("SELECT id_personale_strutturato, ufficio FROM personale_strutturato"))
        eventi = list(sql.execute_query("SELECT id_evento, data FROM evento"))

        for evento in eventi:
            eventi_personale_strutturato = list()
            for _ in range(0, random.randint(1,5)):
                personale_strutturato_random = personale_strutturato[random.randint(0, len(personale_strutturato)-1)][0]

                if personale_strutturato_random not in eventi_personale_strutturato:
                    eventi_personale_strutturato.append(personale_strutturato_random)
            for personale in personale_strutturato_random:
                finanzia_1 = (personale, evento[0], random.randint(500, 1501))
                query = "INSERT INTO dirige VALUES ("
                for value in finanzia_1:
                    query += "'" + str(value) + "',"
                #sql.execute_query(query[:-1] + ")")

creazione_finanzia_1()
