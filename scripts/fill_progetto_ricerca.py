from database_connection import database_connection


def creazione_progetti_ricerca():
    sql = database_connection("bdm_unipa")
    aree_ricerca = sql.execute_query("SELECT id_area_ricerca, nome FROM area_ricerca")
    print(aree_ricerca)



creazione_progetti_ricerca()
