from database_connection import database_connection
import datetime
import random

sql = database_connection("bdm_unimi") #bdm_unipa, bdm_unimi, bdm_unina
pubblicazioni = dict()


def data_random(anno_min, anno_max):
    start_date = datetime.date(anno_min, 1, 1)
    end_date = datetime.date(anno_max, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")


def get_random_area_ricerca():
    result = sql.execute_query("select * from area_ricerca")
    index = random.randrange(len(result))
    return result[index]


def crea_riviste():
    global pubblicazioni
    result = sql.execute_query("select * from area_ricerca")

    for row in result:
        pubblicazioni[row[1]] = list()

    pubblicazioni['Biologia'].append("BioEssays")
    pubblicazioni['Biologia'].append("eLife")

    pubblicazioni['Bioinformatica'].append("BMC Bioinformatics")
    pubblicazioni['Bioinformatica'].append("EMBnet.journal")

    pubblicazioni['Medicina'].append("PLoS Medicine")
    pubblicazioni['Medicina'].append("Annals of Internal Medicine")

    pubblicazioni['Matematica'].append("Acta Mathematica")
    pubblicazioni['Matematica'].append("Annali di Matematica")

    pubblicazioni['Fisica'].append("Acta Crystallographica")
    pubblicazioni['Fisica'].append("Applied Physics Letters")

    pubblicazioni['Farmacia'].append("Annual Review of Immunology")
    pubblicazioni['Farmacia'].append("Nature Reviews Immunology")

    pubblicazioni['Ingegneria'].append("NASA Tech Briefs")
    pubblicazioni['Ingegneria'].append("IEEE Transactions on Computers")

    pubblicazioni['Architettura'].append("ANY")
    pubblicazioni['Architettura'].append("The Architectural Review")

    pubblicazioni['Psicologia'].append("American Journal of Psychiatry")
    pubblicazioni['Psicologia'].append("Diversità culturale ed etnica Psicologia Minority")

    pubblicazioni['Scienze del mare'].append("Journal of Climate")
    pubblicazioni['Scienze del mare'].append("Aquatic Botanica")

    pubblicazioni['Turismo'].append("Turistica Italian Journal of Tourism")
    pubblicazioni['Turismo'].append("Meridiani")

    pubblicazioni['Economia'].append("ZEW – Leibniz Centre for European Economic Research")
    pubblicazioni['Economia'].append("WEF - World Economic Forum")

    pubblicazioni['Informatica'].append("Communications of the ACM")
    pubblicazioni['Informatica'].append("International Journal of Computer Vision")


def get_random_rivista(name):
    index = random.randint(0,1)
    # print(name+" "+str(index))
    return pubblicazioni[name][index]


def creazione_pubblicazioni():
    # V titolo, V data_pubblicazione, nome_rivista, V tipologia, V id_area_ricerca, V indice_qualità
    crea_riviste()
    ran = random.randint(7000,14000)
    for i in range(0, ran):
        area = get_random_area_ricerca()
        pubblicazione = ("Ricerca #"+str(i)+" in "+area[1],
                        data_random(1970, 2020),
                        get_random_rivista(area[1]),
                        "Null",
                        area[0],
                        random.randrange(300)
                        )
        query = "INSERT INTO pubblicazione(titolo,data_pubblicazione,nome_rivista,tipologia,id_area_ricerca,indice_qualita) VALUES ("
        for value in pubblicazione:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")



creazione_pubblicazioni()
