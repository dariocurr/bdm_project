import numpy as np
import random
import string
from database_connection import database_connection


def modifyNamePerson():
    university = list()
    university.append("unipa")
    university.append("unito")
    university.append("unimi")
    university.append("unina")
    for uni in university:
        print("MODIFICA {}".format(uni))
        sql = database_connection("bdm_{}".format(uni))
        name_distinct = sql.execute_query("SELECT DISTINCT nome, cognome FROM personale")
        for name in name_distinct:
            name_tuple = sql.execute_query("SELECT * FROM personale WHERE nome = {}".format("'"+name[0]+"'"))
            if len(name_tuple) > 3:
                entry = list(name_tuple[np.random.randint(0, len(name_tuple))])
                print(entry)
                rnd = np.random.randint(0, 2)
                name_entry = list(entry[1])
                if rnd == 0: #cancellazione
                    name_entry[np.random.randint(0, len(name_entry))] = ''
                    name_entry = "".join(name_entry)
                if rnd == 1: #modifica
                    name_entry[np.random.randint(0, len(name_entry))] = random.choice(string.ascii_letters)
                    name_entry = "".join(name_entry)
                sql.execute_query("UPDATE personale SET nome={} WHERE cf={}".format("'"+ name_entry +"'", "'"+ entry[0] +"'"))


def modifySurnamePerson():
    university = list()
    university.append("unipa")
    university.append("unito")
    university.append("unimi")
    university.append("unina")
    for uni in university:
        print("MODIFICA {}".format(uni))
        sql = database_connection("bdm_{}".format(uni))
        surname_distinct = sql.execute_query("SELECT DISTINCT cognome, nome FROM personale")
        for surname in surname_distinct:
            surname_tuple = sql.execute_query("SELECT * FROM personale WHERE cognome = {}".format("'"+surname[0]+"'"))
            if len(surname_tuple) > 3:
                entry = list(surname_tuple[np.random.randint(0, len(surname_tuple))])
                print(entry)
                rnd = np.random.randint(0, 2)
                surname_entry = list(entry[2])
                if rnd == 0: #cancellazione
                    surname_entry[np.random.randint(0, len(surname_entry))] = ''
                    surname_entry = "".join(surname_entry)
                if rnd == 1: #modifica
                    surname_entry[np.random.randint(0, len(surname_entry))] = random.choice(string.ascii_letters)
                    surname_entry = "".join(surname_entry)
                sql.execute_query("UPDATE personale SET cognome={} WHERE cf={}".format("'"+ surname_entry +"'", "'"+ entry[0] +"'"))


modifyNamePerson()
modifySurnamePerson()
