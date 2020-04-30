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
        for i in range(0, 200):
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

    """
    prefisso_telefono_unipa = "091 238 "
    prefisso_telefono_unito = "011 670 "
    prefisso_telefono_unina = "081 420 "
    prefisso_telefono_unimi = "091 03 "
    livello_stipendio_qualifica = list()
    livello_stipendio_qualifica.append(("B", 1050.45, "Titolo di studio di scuola d’obbligo"))
    livello_stipendio_qualifica.append(("C", 1231.97, "Diploma di scuola superiore"))
    livello_stipendio_qualifica.append(("D", 1767.81, "Diploma di laurea"))
    livello_stipendio_qualifica.append(("EP", 2083.33, "Diploma di laurea e particolare qualificazione personale"))
    tipologia_contratto_strutturato = list()
    tipologia_contratto_strutturato.append("Professore ordinario")
    tipologia_contratto_strutturato.append("Professore associato")
    tipologia_contratto_strutturato.append("Ricercatore a tempo indeterminato")
    tipologia_contratto_strutturato.append("Ricercatore a tempo determinato")
    tipologia_contratto_non_strutturato = list()
    tipologia_contratto_non_strutturato.append("Assegnista")
    tipologia_contratto_non_strutturato.append("Dottorando")
    tipologia_contratto_non_strutturato.append("Contrattista")
    #GENERAZIONE PERSONALE
        telefono = prefisso_telefono_unipa
        #telefono = prefisso_telefono_unito
        #telefono = prefisso_telefono_unina
        #telefono = prefisso_telefono_unimi
        for _ in range(0, 4):
            telefono += str(np.random.randint(0, 10))
        stipendio = (2020 - int(date[:4])) * 6.34
        random_number = np.random.randint(1, 4)
        #PERSONALE TA
        if random_number == 1:
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
        else:
            tipologia_contratto = ""
            stipendio = np.nan
            #PERSONALE STRUTTURATO
            if random_number == 2:
                random_number = np.random.randint(1, 8)
                promozioni = list()
                if random_number < 2:
                    tipologia_contratto = tipologia_contratto_strutturato[0]
                    stipendio += 2550.72
                    prima_promozione_anno_inizio = np.random.randint(1980, 2000)
                    prima_promozione_anno_fine = np.random.randint(prima_promozione_anno_inizio, 2005)
                    vecchio_stipendio = (prima_promozione_anno_fine - int(date[:4])) * 6.34 + 1478.11
                    promozioni.append((str(prima_promozione_anno_inizio) + "/01/01", str(prima_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
                    seconda_promozione_anno_inizio = np.random.randint(prima_promozione_anno_fine, 2010)
                    seconda_promozione_anno_fine = np.random.randint(seconda_promozione_anno_inizio, 2015)
                    vecchio_stipendio = (seconda_promozione_anno_fine - int(date[:4])) * 6.34 + 1802.89
                    promozioni.append((str(seconda_promozione_anno_inizio) + "/01/01", str(seconda_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[2]))
                    terza_promozione_anno_inizio = np.random.randint(seconda_promozione_anno_fine, 2018)
                    terza_promozione_anno_fine = np.random.randint(terza_promozione_anno_inizio, 2019)
                    vecchio_stipendio = (terza_promozione_anno_fine - int(date[:4])) * 6.34 + 2123.19
                    promozioni.append((str(terza_promozione_anno_inizio) + "/01/01", str(terza_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[1]))
                elif random_number < 4:
                    tipologia_contratto = tipologia_contratto_strutturato[1]
                    stipendio += 2123.19
                    prima_promozione_anno_inizio = np.random.randint(1990, 2010)
                    prima_promozione_anno_fine = np.random.randint(prima_promozione_anno_inizio, 2015)
                    vecchio_stipendio = (prima_promozione_anno_fine - int(date[:4])) * 6.34 + 1478.11
                    promozioni.append((str(prima_promozione_anno_inizio) + "/01/01", str(prima_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
                    seconda_promozione_anno_inizio = np.random.randint(prima_promozione_anno_fine, 2018)
                    seconda_promozione_anno_fine = np.random.randint(seconda_promozione_anno_inizio, 2019)
                    vecchio_stipendio = (seconda_promozione_anno_fine - int(date[:4])) * 6.34 + 1802.89
                    promozioni.append((str(seconda_promozione_anno_inizio) + "/01/01", str(seconda_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[2]))
                elif random_number < 6:
                    tipologia_contratto = tipologia_contratto_strutturato[2]
                    stipendio += 1802.89
                    anno_inizio = np.random.randint(2000, 2018)
                    anno_fine = np.random.randint(anno_inizio, 2019)
                    vecchio_stipendio = (anno_fine - int(date[:4])) * 6.34 + 1478.11
                    promozioni.append((str(anno_inizio) + "/01/01", str(anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
                else:
                    tipologia_contratto = tipologia_contratto_strutturato[3]
                    stipendio += 1478.11
                ufficio = np.random.randint(101, 300)
            #PERSONALE NON STRUTTURATO
            else:
                laboratorio_riferimento = "Lab " + str(np.random.randint(1, 100))
    """

creazione_personale()
