from database_connection import database_connection
from faker import Faker

fake = Faker('it_IT')


def creazione_agenzie_esterne():
    sql = database_connection("bdm_unito") #bdm_unipa, bdm_unimi, bdm_unina
    for i in range(0, 50):
        agenzia = (fake.company(), fake.bs(), fake.company_suffix(), fake.address())
        query = "INSERT INTO agenzia_esterna(nome, descrizione, tipologia, indirizzo) VALUES ("
        for value in agenzia:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")



creazione_agenzie_esterne()
