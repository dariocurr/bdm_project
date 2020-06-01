import numpy as np
import pandas as pd
import datetime
import random
from database_connection import database_connection
from codicefiscale import codicefiscale


def data_random(anno_min, anno_max):
    start_date = datetime.date(anno_min, 1, 1)
    end_date = datetime.date(anno_max, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")


def creazione_personale():
    # codice fiscale, nome, cognome, data nascita, residenza, dipartimento
    names = pd.read_csv("../res/datasets/nomi.csv")
    surnames = pd.read_csv("../res/datasets/cognomi.csv")
    hospitals = pd.read_csv("../res/datasets/ospedali.csv")
    cities = pd.read_csv("../res/datasets/comuni.csv", sep=";")
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        dipartimenti = list(sql.execute_query("SELECT id_dipartimento, nome FROM dipartimento"))
        for i in range(0, 500):
            name = names.iloc[np.random.randint(0, 100), 0]
            name = name[0] + str(name[1:]).lower()
            surname = surnames.iloc[np.random.randint(0, 100), 0]
            surname = surname[0] + str(surname[1:]).lower()
            date = data_random(1950, 1992)
            sex = ""
            if name[-1] == "A":
                sex = "F"
            else:
                sex = "M"
            city = hospitals.iloc[np.random.randint(0, len(hospitals)), 1]
            if city.find("/") > 0:
                city = city[:city.find("/")]
            codice_fiscale = codicefiscale.encode(surname=surname, name=name, sex=sex, birthdate=date, birthplace=city)
            city = cities.iloc[np.random.randint(0, len(cities)), 1]
            person = (codice_fiscale, name, surname, date, city, dipartimenti[np.random.randint(0, len(dipartimenti))][0])
            query = "INSERT INTO personale VALUES("
            for value in person:
                query += "'" + str(value) + "',"
            sql.execute_query(query[:-1] + ")")


def creazione_personale_specifico():
    # ta: livello, stipendio, qualifica, telefono, anagrafica_personale
    # ricerca: tipologia_contratto, stipendio, anagrafica_personale, indice_qualita
    # non struttrato: laboratorio_riferimento, telefono, personale_ricerca
    # struttrato: telefono, ufficio, personale_ricerca
    livello_stipendio_qualifica = list()
    livello_stipendio_qualifica.append(("B", 1050.45, "Titolo di studio di scuola d’obbligo"))
    livello_stipendio_qualifica.append(("C", 1231.97, "Diploma di scuola superiore"))
    livello_stipendio_qualifica.append(("D", 1767.81, "Diploma di laurea"))
    livello_stipendio_qualifica.append(("EP", 2083.33, "Diploma di laurea e particolare qualificazione personale"))
    tipologia_contratto_strutturato = list()
    tipologia_contratto_strutturato.append(("Professore ordinario", 2550.72))
    tipologia_contratto_strutturato.append(("Professore associato", 2123.19))
    tipologia_contratto_strutturato.append(("Ricercatore a tempo indeterminato", 1802.89))
    tipologia_contratto_strutturato.append(("Ricercatore a tempo determinato", 1478.11))
    tipologia_contratto_non_strutturato = list()
    tipologia_contratto_non_strutturato.append(("Assegnista", 1323.34))
    tipologia_contratto_non_strutturato.append(("Dottorando", 1231.90))
    tipologia_contratto_non_strutturato.append(("Contrattista", 1002.43))
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        persone = list(sql.execute_query("SELECT cf, data_nascita FROM personale"))
        prefisso = ""
        if db == "bdm_unipa":
            prefisso = "091 238 "
        elif db == "bdm_unito":
            prefisso = "011 670 "
        elif db == "bdm_unina":
            prefisso = "081 420 "
        elif db == "bdm_unimi":
            prefisso = "091 03 "
        for persona in persone:
            telefono = prefisso
            for _ in range(0, 4):
                telefono += str(np.random.randint(0, 10))
            stipendio = (2020 - int(str(persona[1])[:4])) * 6.34
            random_number = np.random.randint(1, 4)
            if random_number == 1:
                #PERSONALE TA
                random_number = np.random.randint(1, 11)
                livello = ""
                qualifica = ""
                if random_number < 4:
                    livello = livello_stipendio_qualifica[0][0]
                    stipendio += livello_stipendio_qualifica[0][1]
                    qualifica = livello_stipendio_qualifica[0][2]
                elif random_number < 8:
                    livello = livello_stipendio_qualifica[1][0]
                    stipendio += livello_stipendio_qualifica[1][1]
                    qualifica = livello_stipendio_qualifica[1][2]
                elif random_number < 10:
                    livello = livello_stipendio_qualifica[2][0]
                    stipendio += livello_stipendio_qualifica[2][1]
                    qualifica = livello_stipendio_qualifica[2][2]
                else:
                    livello = livello_stipendio_qualifica[3][0]
                    stipendio += livello_stipendio_qualifica[3][1]
                    qualifica = livello_stipendio_qualifica[3][2]
                ta = (livello, stipendio, qualifica, telefono, persona[0])
                query = "INSERT INTO personale_ta(livello, stipendio, qualifica, telefono, anagrafica_personale) VALUES("
                for value in ta:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")
            else:
                #PERSONALE_RICERCA
                tipologia_contratto = ""
                if random_number == 2:
                    #PERSONALE STRUTTURATO
                    random_number = np.random.randint(1, 8)
                    if random_number < 2:
                        tipologia_contratto = tipologia_contratto_strutturato[0][0]
                        stipendio += tipologia_contratto_strutturato[0][1]
                    elif random_number < 4:
                        tipologia_contratto = tipologia_contratto_strutturato[1][0]
                        stipendio += tipologia_contratto_strutturato[1][1]
                    elif random_number < 6:
                        tipologia_contratto = tipologia_contratto_strutturato[2][0]
                        stipendio += tipologia_contratto_strutturato[2][1]
                    else:
                        tipologia_contratto = tipologia_contratto_strutturato[3][0]
                        stipendio += tipologia_contratto_strutturato[3][1]
                    ricerca = (tipologia_contratto, stipendio, persona[0], np.random.randint(1, 11))
                    query = "INSERT INTO personale_ricerca(tipologia_contratto, stipendio, anagrafica_personale, indice_qualita) VALUES("
                    for value in ricerca:
                        query += "'" + str(value) + "',"
                    sql.execute_query(query[:-1] + ")")
                    ufficio = np.random.randint(101, 300)
                    query = "SELECT id_personale_ricerca, stipendio FROM personale_ricerca WHERE anagrafica_personale = \"" + str(persona[0]) + "\""
                    result = list(sql.execute_query(query))
                    strutturato = (telefono, ufficio, result[0][0])
                    query = "INSERT INTO personale_strutturato(telefono, ufficio, personale_ricerca) VALUES("
                    for value in strutturato:
                        query += "'" + str(value) + "',"
                    sql.execute_query(query[:-1] + ")")
                else:
                    #PERSONALE NON STRUTTURATO
                    random = np.random.randint(0, 3)
                    tipologia_contratto = tipologia_contratto_non_strutturato[random][0]
                    stipendio += tipologia_contratto_non_strutturato[random][1]
                    ricerca = (tipologia_contratto, stipendio, persona[0], np.random.randint(1, 11))
                    query = "INSERT INTO personale_ricerca(tipologia_contratto, stipendio, anagrafica_personale, indice_qualita) VALUES("
                    for value in ricerca:
                        query += "'" + str(value) + "',"
                    sql.execute_query(query[:-1] + ")")
                    laboratorio_riferimento = "Lab " + str(np.random.randint(1, 100))
                    query = "SELECT id_personale_ricerca, stipendio FROM personale_ricerca WHERE anagrafica_personale = \"" + str(persona[0]) + "\""
                    result = list(sql.execute_query(query))
                    non_strutturato = (laboratorio_riferimento, telefono, result[0][0])
                    query = "INSERT INTO personale_non_strutturato(laboratorio_riferimento, telefono, personale_ricerca) VALUES("
                    for value in non_strutturato:
                        query += "'" + str(value) + "',"
                    sql.execute_query(query[:-1] + ")")
