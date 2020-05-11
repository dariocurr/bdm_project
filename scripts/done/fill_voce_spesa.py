from database_connection import database_connection
import datetime
import random
import numpy as np


def data_random(anno_min, anno_max):
    start_date = datetime.date(anno_min, 1, 1)
    end_date = datetime.date(anno_max, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")


def creazione_voce_spesa():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        voce_fondo = list(sql.execute_query("SELECT id_voce_fondo, nome, importo, fondo FROM voce_fondo"))
        progetti_ricerca = list()
        manutenzione = list()
        attrezzatura = list()
        eventi = list()
        personale = list()
        for voce in voce_fondo:
            if voce[1] == "manutenzione":
                manutenzione.append(voce)
            elif voce[1] == "attrezzatura":
                attrezzatura.append(voce)
            elif voce[1] == "eventi":
                eventi.append(voce)
            elif voce[1] == "progetti e ricerca":
                progetti_ricerca.append(voce)
            elif voce[1] == "personale":
                personale.append(voce)
        voci_spesa = list()
        for voce in manutenzione:
            data = sql.execute_query("SELECT id_fondo, data FROM fondo WHERE id_fondo = " + str(voce[3]))[0][1]
            fondi = float(voce[2])
            while fondi > 1000:
                spesa = round(np.random.randint(0, fondi) + np.random.uniform(), 2)
                voce_spesa = (voce[1], "Spesa relativa a " + voce[1], spesa, voce[0], data_random(int(str(data)[0:4]) + 1, 2020))
                voci_spesa.append(voce_spesa)
                fondi -= spesa
        for voce in attrezzatura:
            data = sql.execute_query("SELECT id_fondo, data FROM fondo WHERE id_fondo = " + str(voce[3]))[0][1]
            fondi = float(voce[2])
            while fondi > 1000:
                spesa = round(np.random.randint(0, fondi) + np.random.uniform(), 2)
                voce_spesa = (voce[1], "Spesa relativa a " + voce[1], spesa, voce[0], data_random(int(str(data)[0:4]) + 1, 2020))
                voci_spesa.append(voce_spesa)
                fondi -= spesa
        for voce in eventi:
            data = sql.execute_query("SELECT id_fondo, data FROM fondo WHERE id_fondo = " + str(voce[3]))[0][1]
            fondi = float(voce[2])
            while fondi > 1000:
                spesa = round(np.random.randint(0, 100000) + np.random.uniform(), 2)
                voce_spesa = ("evento", "Spesa relativa a evento", spesa, voce[0], data_random(int(str(data)[0:4]) + 1, 2020))
                voci_spesa.append(voce_spesa)
                fondi -= spesa
        for voce in progetti_ricerca:
            data = sql.execute_query("SELECT id_fondo, data FROM fondo WHERE id_fondo = " + str(voce[3]))[0][1]
            fondi = float(voce[2])
            while fondi > 1000:
                spesa = round(np.random.randint(0, 100000) + np.random.uniform(), 2)
                voce_spesa = ("progetto ricerca", "Spesa relativa a progetto ricerca", spesa, voce[0], data_random(int(str(data)[0:4]) + 1, 2020))
                voci_spesa.append(voce_spesa)
                fondi -= spesa
        retribuisce = list()
        personale_non_strutturato = list(sql.execute_query("SELECT id_personale_non_strutturato, stipendio FROM personale_non_strutturato, personale_ricerca WHERE personale_non_strutturato.personale_ricerca = personale_ricerca.id_personale_ricerca"))
        for voce in personale:
            data = sql.execute_query("SELECT id_fondo, data FROM fondo WHERE id_fondo = " + str(voce[3]))[0][1]
            fondi = float(voce[2])
            while fondi > 1000:
                for personale in personale_non_strutturato:
                    if fondi > 1000:
                        stipendio = float(personale[1])
                        voce_spesa = ("personale", "Spesa relativa a personale", stipendio, voce[0], data_random(int(str(data)[0:4]) + 1, 2020))
                        retribuisce.append((voce_spesa, personale[0]))
                        fondi -= stipendio
        for voce in voci_spesa:
            query = "INSERT INTO voce_spesa(nome, descrizione, importo, copertura, data) VALUES ("
            for value in voce:
                query += "'" + str(value) + "',"
            sql.execute_query(query[:-1] + ")")
        for voce in retribuisce:
            query = "INSERT INTO voce_spesa(nome, descrizione, importo, copertura, data) VALUES ("
            for value in voce[0]:
                query += "'" + str(value) + "',"
            sql.execute_query(query[:-1] + ")")
            query = "SELECT id_voce_spesa, importo FROM voce_spesa WHERE importo = " + str(voce[0][2]) + " AND data = \'" + str(voce[0][4]) + "\'"
            voce_spesa = sql.execute_query(query)
            t = (voce_spesa[0][0], voce[1])
            query = "INSERT INTO retribuisce VALUES ("
            for value in t:
                query += "'" + str(value) + "',"
            sql.execute_query(query[:-1] + ")")


creazione_voce_spesa()
