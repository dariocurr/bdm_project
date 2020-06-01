from database_connection import database_connection
import random
import math


def update_hindex():
    sql = database_connection("bdm_uni_riconciliato")
    personale_ricerca = sql.execute_query("SELECT id_personale_ricerca FROM personale_ricerca")
    """pubblicazioni = sql.execute_query("SELECT id_pubblicazione, indice_qualita FROM pubblicazioni")
    pubblica = sql.execute_query("SELECT * FROM pubblica")"""
    for persone in personale_ricerca:
        mean = 0
        pubblicazioni = sql.execute_query("SELECT pubblicazione.indice_qualita FROM pubblicazione JOIN pubblica ON pubblicazione.id_pubblicazione = pubblica.pubblicazione WHERE pubblica.personale_ricerca = "+str(persone[0]))
        for pubblicazione in pubblicazioni:
            mean += pubblicazione[0]
        query = "UPDATE personale_ricerca SET indice_qualita = {} WHERE id_personale_ricerca = {}".format(math.floor((mean/len(pubblicazioni))), persone[0])
        sql.execute_query(query)


update_hindex()
