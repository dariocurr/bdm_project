import numpy as np
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


# ha bisogno di dipartimento ed i nomi che prendiamo dai file sono senza senso
def creazione_fondo():
    # nome, budget, data, ente, dipartimento
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        dipartimenti = list(sql.execute_query("SELECT id_dipartimento, nome FROM dipartimento"))
        enti = list(sql.execute_query("SELECT id_ente, nome FROM ente"))
        for ente in enti:
            num = np.random.randint(1, len(dipartimenti))
            fondi = list()
            while num > 0:
                fondi.append(("universale", round(np.random.randint(10000, 1000000) + np.random.uniform(), 2),
                            data_random(2000, 2019), ente[0], dipartimenti[np.random.randint(0, len(dipartimenti))][0]))
                num -= 1
            for fondo in fondi:
                query = "INSERT INTO fondo(nome, budget, data, ente, dipartimento) VALUES ("
                for value in fondo:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")


creazione_fondo()
