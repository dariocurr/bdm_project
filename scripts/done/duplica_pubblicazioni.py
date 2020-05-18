from database_connection import database_connection
import random
import math

sql = database_connection("bdm_unito") #bdm_unipa, bdm_unimi, bdm_unina
pubblicazioni = sql.execute_query("select titolo,data_pubblicazione,nome_rivista,tipologia,id_area_ricerca,indice_qualita from pubblicazione")


def duplica():
    r = 0.01
    n = int(math.floor(len(pubblicazioni)*r))
    for i in range(0, n):
        index = random.randint(0,len(pubblicazioni))
        row = pubblicazioni[index]

        query = "INSERT INTO pubblicazione(titolo,data_pubblicazione,nome_rivista,tipologia,id_area_ricerca,indice_qualita) VALUES ("
        for value in row:
            query += "'" + str(value) + "',"
        print(query[:-1] + ")")
        sql.execute_query(query[:-1] + ")")

duplica();
