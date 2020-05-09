import random
from database_connection import database_connection



def creazione_dirige():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        personale_strutturato = list(sql.execute_query("SELECT id_personale_strutturato, telefono FROM personale_strutturato"))
        progetto_ricerca = list(sql.execute_query("SELECT id_progetto, data_avvio FROM progetto_ricerca"))

        #print(personale_strutturato[1])
        for progetto in progetto_ricerca:
            professori_progetto = list()

            for _ in range(0, random.randint(1,2)):

                professore_random = personale_strutturato[random.randint(0, len(personale_strutturato)-1)][0]

                if professore_random not in professori_progetto:
                    professori_progetto.append(professore_random)
            for professore in professori_progetto:
                dirige = (professore, progetto[0], progetto[1])
                query = "INSERT INTO dirige VALUES ("
                for value in dirige:
                    query += "'" + str(value) + "',"
                sql.execute_query(query[:-1] + ")")





creazione_dirige()
