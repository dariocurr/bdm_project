from database_connection import database_connection


def fill_organizza():
    university = list()
    university.append("unipa")
    university.append("unito")
    university.append("unimi")
    university.append("unina")
    for uni in university:
        #personale_strutturato, evento
        print("INSERIMENTO {}".format(uni))
        sql = database_connection("bdm_{}".format(uni))
        id_personale_strutturato = sql.execute_query("SELECT id_personale_strutturato, ufficio FROM personale_strutturato WHERE 1")
        id_evento = sql.execute_query("SELECT id_evento, argomento FROM evento WHERE 1")
        for evento in id_evento:
            n_rnd = np.random.randint(2, 6)
            for _ in range(1, n_rnd):
                id_personale = np.random.randint(0, len(id_personale_strutturato))
                print("INSERT INTO organizza(personale_strutturato, evento) VALUES({},{})".format(id_personale_strutturato[id_personale][0], evento[0]))
