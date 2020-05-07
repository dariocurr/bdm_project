import numpy as np
from database_connection import database_connection


def create_partecipa_2():
    university = list()
    university.append("unipa")
    university.append("unito")
    university.append("unimi")
    university.append("unina")
    for uni in university:
        sql = database_connection("bdm_{}".format(uni))
        print("Università: {}".format(uni))
        id_progetto = list(sql.execute_query("SELECT id_progetto FROM progetto_ricerca WHERE 1"))
        personale_ricerca = list(sql.execute_query("SELECT id_personale_ricerca, tipologia_contratto FROM personale_ricerca WHERE 1"))
        ruolo = ["tecnico progetto", "assistente", "dirigente"]
        for id in id_progetto:
            id = str(id)[1:].replace(",", "")
            id = id.replace(")", "").strip()
            professori = list()
            rnd = np.random.randint(1, 5)
            while len(professori) < rnd:
                prof = personale_ricerca[np.random.randint(0, len(personale_ricerca))][0]
                if prof not in professori:
                    professori.append(prof)
            for id_personale in professori:
                sql.execute_query("INSERT INTO partecipa_2(personale_ricerca, progetto_ricerca, ruolo) VALUES({},{},{})".format(id_personale, id,  "'"+ruolo[np.random.randint(0, len(ruolo))]+"'"))
        print("FINE CARICAMENTO")


create_partecipa_2()
