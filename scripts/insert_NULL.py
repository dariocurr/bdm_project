from database_connection import database_connection
import random
import math


def insert_NULL():
    for db in ["bdm_uni_riconciliato"]:
        sql = database_connection(db)
        agenzia_esterna = sql.execute_query("SELECT id_agenzia, nome, descrizione, tipologia, indirizzo FROM agenzia_esterna")
        for i in range(0, math.ceil((len(agenzia_esterna))*5/100)):
            a = random.randint(0, 2)
            query = ""
            if a == 0:
                query = "UPDATE agenzia_esterna SET indirizzo = NULL WHERE id_agenzia = {}".format(agenzia_esterna[random.randint(0, len(agenzia_esterna)-1)][0])
            elif a == 1:
                query = "UPDATE agenzia_esterna SET descrizione = NULL WHERE id_agenzia = {}".format(agenzia_esterna[random.randint(0, len(agenzia_esterna)-1)][0])
            elif a == 2:
                query = "UPDATE agenzia_esterna SET tipologia = NULL WHERE id_agenzia = {}".format(agenzia_esterna[random.randint(0, len(agenzia_esterna)-1)][0])
            sql.execute_query(query)


insert_NULL()
