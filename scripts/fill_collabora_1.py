from database_connection import database_connection


def fill_collabora_1():
    university = list()
    university.append("unipa")
    university.append("unito")
    university.append("unimi")
    university.append("unina")
    for uni in university:
        #personale, evento, ruolo
        print("INSERIMENTO {}".format(uni))
        sql = database_connection("bdm_{}".format(uni))
        id_personale = sql.execute_query("SELECT id_personale_ricerca, tipologia_contratto FROM personale_ricerca WHERE 1")
        id_evento = sql.execute_query("SELECT id_evento, argomento FROM evento WHERE 1")
        for evento in id_evento:
            n_rnd = np.random.randint(2, 6)
            for _ in range(1, n_rnd):
                id_personale_rnd = np.random.randint(0, len(id_personale))
                print("INSERT INTO collabora_1(personale, evento) VALUES({},{})".format(id_personale[id_personale_rnd][0], evento[0]))

fill_collabora_1()
