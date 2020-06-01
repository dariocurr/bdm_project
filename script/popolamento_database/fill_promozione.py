import numpy as np
import pandas as pd
import datetime
import random
from database_connection import database_connection


def data_random(anno_min, anno_max):
    start_date = datetime.date(anno_min, 1, 1)
    end_date = datetime.date(anno_max, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")

def creazione_promozioni():
    tipologia_contratto_strutturato = list()
    tipologia_contratto_strutturato.append(("Ricercatore a tempo determinato", 1478.11))
    tipologia_contratto_strutturato.append(("Ricercatore a tempo indeterminato", 1802.89))
    tipologia_contratto_strutturato.append(("Professore associato", 2123.19))
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        promozioni = list()
        sql = database_connection(db)
        personale = list(sql.execute_query("SELECT id_personale_ricerca, tipologia_contratto FROM personale_ricerca"))
        for persona in personale:
            if persona[1] == "Professore ordinario":
                anno_fine = np.random.randint(1980, 1990)
                for i in range(0, 3):
                    anno_inizio = anno_fine
                    anno_fine = anno_inizio + np.random.randint(0, 11)
                    stipendio = round(tipologia_contratto_strutturato[i][1] + np.random.randint(1, 100) + np.random.uniform(), 2)
                    promozioni.append((anno_inizio, anno_fine, stipendio, tipologia_contratto_strutturato[i][0], persona[0]))
                    anno_inizio = anno_fine
            elif persona[1] == "Professore associato":
                anno_fine = np.random.randint(1980, 2000)
                for i in range(0, 2):
                    anno_inizio = anno_fine
                    anno_fine = anno_inizio + np.random.randint(0, 11)
                    stipendio = round(tipologia_contratto_strutturato[i][1] + np.random.randint(1, 100) + np.random.uniform(), 2)
                    promozioni.append((anno_inizio, anno_fine, stipendio, tipologia_contratto_strutturato[i][0], persona[0]))
                    anno_inizio = anno_fine
            elif persona[1] == "Ricercatore a tempo indeterminato":
                anno_fine = np.random.randint(1980, 2010)
                for i in range(0, 1):
                    anno_inizio = anno_fine
                    anno_fine = anno_inizio + np.random.randint(0, 11)
                    stipendio = round(tipologia_contratto_strutturato[i][1] + np.random.randint(1, 100) + np.random.uniform(), 2)
                    promozioni.append((anno_inizio, anno_fine, stipendio, tipologia_contratto_strutturato[i][0], persona[0]))
                    anno_inizio = anno_fine
        for promozione in promozioni:
            query = "INSERT INTO promozione(data_inizio, data_fine, stipendio, tipologia_contratto, personale_ricerca) VALUES("
            for value in promozione:
                query += "'" + str(value) + "',"
            sql.execute_query(query[:-1] + ")")
            

creazione_promozioni()
