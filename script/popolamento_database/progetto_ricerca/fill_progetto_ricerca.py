import datetime
import random
import numpy as np
import pymysql.cursors
from database_connection import database_connection


def data_random(anno_min, anno_max):
    start_date = datetime.date(anno_min, 1, 1)
    end_date = datetime.date(anno_max, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")


def creazione_progetti_ricerca():
    # nome, descrizione, data_avvio, data_fine, budget, area_ricerca
    university = list()
    university.append("unipa")
    university.append("unito")
    university.append("unimi")
    university.append("unina")
    for uni in university:
        print("INSERIMENTO {}".format(uni))
        sql = database_connection("bdm_{}".format(uni))
        aree_ricerca = list(sql.execute_query("SELECT id_area_ricerca, nome FROM area_ricerca"))
        #print(aree_ricerca)
        progetti_ricerca = list()
        file = open("{}.txt".format(uni), "r")
        text = file.readline()
        while text != "":
            abstract = file.readline()
            index = get_area_ricerca(abstract)
            if abstract == "//\n":
                abstract = ""
            progetti_ricerca.append((text, abstract, data_random(2012, 2015), data_random(2016, 2021), np.random.randint(0, 10000), aree_ricerca[index][0]))
            text = file.readline()
        file.close()
        prova = ""
        for progetti in progetti_ricerca:
            prova = "INSERT INTO progetto_ricerca(nome, descrizione, data_avvio, data_fine, budget, id_area_ricerca) VALUES({},{},{},{},{},{})".format("'"+progetti[0]+"'", "'"+progetti[1]+"'", "'"+progetti[2]+"'", "'"+progetti[3]+"'", progetti[4], progetti[5])
            sql.execute_query(prova)
        print("FINE INSERIMENTO")


def get_area_ricerca(text):
    text = text.lower()
    if text.find("biologia") != -1 or text.find("biological") != -1 or text.find("biology") != -1:
        return 0
    if text.find("bioinformatica") != -1 or text.find("bioinformatiche") != -1:
        return 1
    if text.find("medicina") != -1 or text.find("medicine") != -1 or text.find("biomedicine") != -1 or text.find("medical") != -1:
        return 2
    if text.find("matematica") != -1 or text.find("mathematical") != -1:
        return 3
    if text.find("fisica") != -1:
        return 4
    if text.find("farmacia") != -1:
        return 5
    if text.find("ingegneria") != -1:
        return 6
    if text.find("architettura") != -1 or text.find("architectures") != -1 or text.find("architecture") != -1:
        return 7
    if text.find("economia") != -1 or text.find("economy") != -1:
        return 8
    if text.find("psicologia") != -1 or text.find("psicology") != -1:
        return 9
    if text.find("scienze del mare") != -1 or text.find("mare") != -1:
        return 10
    if text.find("turismo") != -1:
        return 11
    if text.find("informatica") != -1 or text.find("informatics") != -1 or text.find("network") != -1:
        return 12
    rnd = np.random.randint(0, 12)
    return rnd

creazione_progetti_ricerca()
