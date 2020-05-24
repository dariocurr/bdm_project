from database_connection import database_connection
import random
import math


def insert_NULL():
    for db in ["bdm_uni_riconciliato"]:
        sql = database_connection(db)
        agenzia_esterna = sql.execute_query("SELECT id_agenzia, nome, descrizione, tipologia, indirizzo FROM agenzia_esterna")
        personale_non_strutturato = sql.execute_query("SELECT id_personale_non_strutturato, laboratorio_riferimento, telefono FROM personale_non_strutturato")
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


        for i in range(0, math.ceil((len(personale_non_strutturato))*5/100)):
            a = random.randint(0, 1)
            query = ""
            if a == 0:
                query = "UPDATE personale_non_strutturato SET laboratorio_riferimento = NULL WHERE id_personale_non_strutturato = {}".format(personale_non_strutturato[random.randint(0, len(personale_non_strutturato)-1)][0])
            elif a == 1:
                query = "UPDATE personale_non_strutturato SET telefono = NULL WHERE id_personale_non_strutturato = {}".format(personale_non_strutturato[random.randint(0, len(personale_non_strutturato)-1)][0])

            #sql.execute_query(query)
            #print(query)


insert_NULL()
