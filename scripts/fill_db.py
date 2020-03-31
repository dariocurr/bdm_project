import datetime
import random
import numpy as np
import pandas as pd
from codicefiscale import codicefiscale


names = pd.read_csv("../res/datasets/nomi.csv")
surnames = pd.read_csv("../res/datasets/cognomi.csv")
hospitals = pd.read_csv("../res/datasets/ospedali.csv")
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

for i in range(0, 100):
    name = names.iloc[np.random.randint(0, 100), 0]
    surname = surnames.iloc[np.random.randint(0, 100), 0]
    day = np.random.randint(1, 32)
    month = np.random.randint(1, 13)
    year = np.random.randint(1950, 1995)
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(1992, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    date = str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")
    sex = ""
    if name[-1] == "A":
        sex = "F"
    else:
        sex = "M"
    city = hospitals.iloc[np.random.randint(0, len(hospitals)), 1]
    if city.find("/") > 0:
        city = city[:city.find("/")]
    codice_fiscale = codicefiscale.encode(surname=surname, name=name, sex=sex, birthdate=date, birthplace=city)
    telefono = ""
    for _ in range(0, 5):
        telefono += str(np.random.randint(0, 10))
    random_number = np.random.randint(1, 4)
    if random_number == 1:
        random_number = np.random.randint(1, 11)
        livello = ""
        stipendio = np.nan
        qualifica = ""
        if random_number < 4:
            livello = livello_stipendio_qualifica[0][0]
            stipendio = livello_stipendio_qualifica[0][1]
            qualifica = livello_stipendio_qualifica[0][2]
        elif random_number < 8:
            livello = livello_stipendio_qualifica[1][0]
            stipendio = livello_stipendio_qualifica[1][1]
            qualifica = livello_stipendio_qualifica[1][2]
        elif random_number < 10:
            livello = livello_stipendio_qualifica[2][0]
            stipendio = livello_stipendio_qualifica[2][1]
            qualifica = livello_stipendio_qualifica[2][2]
        else:
            livello = livello_stipendio_qualifica[3][0]
            stipendio = livello_stipendio_qualifica[3][1]
            qualifica = livello_stipendio_qualifica[3][2]
    else:
        tipologia_contratto = ""
        stipendio = ""
        if random_number == 2:
            #random_number = np.random.randint(1, )
            print("personale_strutturato")
        else:
            print("personale_non_strutturato")

    #unipa 091 238
    #unito 011 670
    #unina 081 420
    #unimi 025 03
