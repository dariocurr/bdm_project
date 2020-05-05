import datetime
import random
import numpy as np
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
    sql = database_connection("bdm_unipa")
    aree_ricerca = list(sql.execute_query("SELECT id_area_ricerca, nome FROM area_ricerca"))
    progetti_ricerca = list()
    for i in range(0, len(aree_ricerca)):
        if "informatica" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2012, 2015), data_random(2016, 2021), np.random.randint(0, 10000), aree_ricerca[i][0]))
        if "economia" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2011, 2014), data_random(2015, 2021), np.random.randint(0, 10000), aree_ricerca[i][0]))
        if "ingegneria" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2012, 2013), data_random(2014, 2020), np.random.randint(0, 10000), aree_ricerca[i][0]))
        if "architettura" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2010, 2013), data_random(2014, 2022), np.random.randint(0, 10000), aree_ricerca[i][0]))
        if "psicologia" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2014, 2016), data_random(2017, 2023), np.random.randint(0, 10000), aree_ricerca[i][0]))
        if "medicina" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2013, 2017), data_random(2018, 2025), np.random.randint(0, 10000), aree_ricerca[i][0]))
        if "farmacia" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2010, 2013), data_random(2014, 2021), np.random.randint(0, 10000), aree_ricerca[i][0]))
        if "fisica" in str(aree_ricerca[i][1]).lower():
            progetti_ricerca.append(("", "", data_random(2012, 2013), data_random(2013, 2021), np.random.randint(0, 10000), aree_ricerca[i][0]))


creazione_progetti_ricerca()
