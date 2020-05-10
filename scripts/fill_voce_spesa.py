from database_connection import database_connection


def creazione_voce_spesa():
    for db in ["bdm_unipa", "bdm_unina", "bdm_unito", "bdm_unimi"]:
        sql = database_connection(db)
        voce_fondo = list(sql.execute_query("SELECT id_voce_fondo, nome, importo, fondo FROM voce_fondo"))
        progetti_ricerca = list()
        manutenzione = list()
        attrezzatura = list()
        eventi = list()
        personale = list()
        for voce in voce_fondo:
            if voce[1] == "manutenzione":
                manutenzione.append(voce)
            elif voce[1] == "attrezzatura":
                attrezzatura.append(voce)
            elif voce[1] == "eventi":
                eventi.append(voce)
            elif voce[1] == "progetti e ricerca":
                progetti_ricerca.append(voce)
            elif voce[1] == "personales":
                personale.append(voce)


creazione_voce_spesa()
