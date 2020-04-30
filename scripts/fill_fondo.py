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


# ha bisogno di dipartimento ed i nomi che prendiamo dai file sono senza senso
def creazione_fondo():
    #nome, budget, data, ente, dipartimento
    founds = pd.read_csv("../res/datasets/contributi_atenei.csv", sep=";")
    fondi_palermo = list()
    fondi_torino = list()
    fondi_napoli = list()
    fondi_milano = list()
    #TORINO
    sql = database_connection("bdm_unito")
    enti_torino = sql.execute_query("SELECT id_ente, nome FROM ente")
    enti_torino = list(enti_torino)
    for i in range(0, 11):
        fondi_torino.append((founds.iloc[i, 4], founds.iloc[i, 5], data_random(1990, 2020), enti_torino[np.random.randint(0, len(enti_torino))][0]))
    for fondo in fondi_torino:
        query = "INSERT INTO fondo(nome, budget, data, ente) VALUES ("
        for value in fondo:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    #MILANO
    sql = database_connection("bdm_unimi")
    enti_milano = sql.execute_query("SELECT id_ente, nome FROM ente")
    enti_milano = list(enti_milano)
    for i in range(0, 11):
        fondi_milano.append((founds.iloc[11+i, 4], founds.iloc[11+i, 5], data_random(1990, 2020), enti_milano[np.random.randint(0, len(enti_milano))][0]))
    for fondo in fondi_milano:
        query = "INSERT INTO fondo(nome, budget, data, ente) VALUES ("
        for value in fondo:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    #NAPOLI
    sql = database_connection("bdm_unina")
    enti_napoli = sql.execute_query("SELECT id_ente, nome FROM ente")
    enti_napoli = list(enti_napoli)
    for i in range(0, 11):
        fondi_napoli.append((founds.iloc[22+i, 4], founds.iloc[22+i, 5], data_random(1990, 2020), enti_napoli[np.random.randint(0, len(enti_napoli))][0]))
    for fondo in fondi_napoli:
        query = "INSERT INTO fondo(nome, budget, data, ente) VALUES ("
        for value in fondo:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    #PALERMO
    sql = database_connection("bdm_unipa")
    enti_palermo = sql.execute_query("SELECT id_ente, nome FROM ente")
    enti_palermo = list(enti_palermo)
    for i in range(0, 11):
        fondi_palermo.append((founds.iloc[33+i, 4], founds.iloc[33+i, 5], data_random(1990, 2020), enti_palermo[np.random.randint(0, len(enti_palermo))][0]))
    for fondo in fondi_palermo:
        query = "INSERT INTO fondo(nome, budget, data, ente) VALUES ("
        for value in fondo:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
