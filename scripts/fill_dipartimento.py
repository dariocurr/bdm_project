from database_connection import database_connection
#DAFARE
def creazione_dipartimenti():
    #GENERAZIONE DIPARTIMENTI
    #ID_Dipartimento, Nome, indirizzo
    dipartimenti_unito = list()
    dipartimenti_unito.append(("Dipartimento di Biotecnologie Molecolari e Scienze per la Salute","Via Nizza, 52, 10126, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Chimica", "Via Pietro Giuria, 7, 10125, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Culture, Politica e Societa","Lungo Dora Siena, 100 A, 10153, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Economia e Statistica Cognetti de Martiis","Lungo Dora Siena, 100 A, 10153, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Filosofia e Scienze dell’Educazione","Via S. Ottavio, 20, 10124, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Fisica","Via P. Giuria, 1, 10125, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Giurisprudenza","Lungo Dora Siena, 100 A, 10153, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Informatica","Corso Svizzera, 185, 10149, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Lingue e Letterature straniere e Culture moderne","Complesso Aldo Moro - via Verdi, fronte civico 41 - Torino"))
    dipartimenti_unito.append(("Dipartimento di Management","Corso Unione Sovietica, 218 Bis, 10134, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Matematica \"Giuseppe Peano\"","Via Carlo Alberto, 10, 10123, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Neuroscienze \"Rita Levi Montalcini\"","Via Cherasco, 15, 10126, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Oncologia","Regione Gonzole, 10, 10043, Orbassano, TO"))
    dipartimenti_unito.append(("Dipartimento di Psicologia","Via Verdi, 10, 10124, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienza e Tecnologia del Farmaco","Via P. Giuria, 9, 10125, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze Agrarie, Forestali e Alimentari","Largo Paolo Braccini, 2, 10095, Grugliasco, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze Chirurgiche","Corso Dogliotti, 14, 10126, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze Cliniche e Biologiche","Regione Gonzole, 10, 10043, Orbassano, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze della Sanità Pubblica e Pediatriche","Piazza Polonia, 94, 10126, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze della Terra","Via Valperga Caluso, 35, 10125, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze della Vita e Biologia dei Sistemi","Via Accademia Albertina, 13, 10123, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze economico-sociali e matematico-statistiche","Corso Unione Sovietica, 218 Bis, 10134, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze Mediche","Corso Dogliotti, 14, 10126, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Scienze Veterinarie","Largo Paolo Braccini, 2, 10095, Grugliasco, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Studi Storici","Via S. Ottavio, 20, 10124, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento di Studi Umanistici","Via S. Ottavio, 20, 10124, Torino, TO"))
    dipartimenti_unito.append(("Dipartimento Interateneo di Scienze, Progetto e Politiche del Territorio","Viale Mattioli, 39, 10125, Torino, TO"))
    #UNIPA
    dipartimenti_unipa = list()
    dipartimenti_unipa.append(("Architettura","Viale delle Scienze, Ed. 14"))
    dipartimenti_unipa.append(("Biomedicina, Neuroscienze e Diagnostica avanzata","Via del Vespro, 129"))
    dipartimenti_unipa.append(("Culture e Società","Viale delle Scienze, Ed. 15"))
    dipartimenti_unipa.append(("Discipline Chirurgiche, Oncologiche e Stomatologiche","Via Liborio Giuffrè, 5"))
    dipartimenti_unipa.append(("Fisica e Chimica - Emilio Segrè","Viale delle Scienze, Ed. 17"))
    dipartimenti_unipa.append(("Giurisprudenza","Via Maqueda, 172"))
    dipartimenti_unipa.append(("Ingegneria","Viale delle Scienze, Ed. 8"))
    dipartimenti_unipa.append(("Matematica e Informatica","Via Archirafi, 34"))
    dipartimenti_unipa.append(("Promozione della Salute, Materno-Infantile, di Medicina Interna e Specialistica di Eccellenza \“G. D’Alessandro\”","Piazza delle Cliniche, 2"))
    dipartimenti_unipa.append(("Scienze Agrarie, Alimentari e Forestali","Viale delle Scienze, Ed. 4"))
    dipartimenti_unipa.append(("Scienze della Terra e del Mare","Via Archirafi, 22"))
    dipartimenti_unipa.append(("Scienze e Tecnologie Biologiche Chimiche e Farmaceutiche","Viale delle Scienze, Ed. 16"))
    dipartimenti_unipa.append(("Scienze Economiche, Aziendali e Statistiche","Viale delle Scienze, Ed. 13"))
    dipartimenti_unipa.append(("Scienze Politiche e delle relazioni internazionali","Via Maqueda, 324"))
    dipartimenti_unipa.append(("Scienze Psicologiche, Pedagogiche, dell’Esercizio Fisico e della Formazione","Viale delle Scienze, Ed. 15"))
    dipartimenti_unipa.append(("Scienze Umanistiche","Viale delle Scienze, Ed. 12"))

    #milano
    dipartimenti_unimi = list()
    dipartimenti_unimi.append(("Dipartimento di Beni Culturali e Ambientali","Via Festa del Perdono 720122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Bioscienze","Via Celoria 26 20133 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Biotecnologie Mediche e Medicina Traslazionale","Via Vanvitelli 32 20133 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Chimica","Via Golgi 19 20133 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Diritto Privato e Storia del Diritto","Via Festa del Perdono 7 20122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Diritto Pubblico Italiano e Sovranazionale","Via Festa del Perdono 7 20122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Economia, Management e Metodi Quantitativi","Via Conservatorio 7 20122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Filosofia Piero Martinetti","Via Festa del Perdono 7 20122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Fisiopatologia Medico-Chirurgica e dei Trapianti","Via Francesco Sforza 35 20122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Fisica Aldo Pontremoli","Via Celoria 16 20133 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Informatica Giovanni degli Antoni","Via Celoria 18 20135 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Lingue e Letterature Straniere","Piazza Sant Alessandro 1 20122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Matematica Federigo Enriques","Via Saldini 50 20129 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Medicina Veterinaria","Lodi - Via dell Università 6 26900 Lodi"))
    dipartimenti_unimi.append(("Dipartimento di Scienze Agrarie e Ambientali - Produzione, Territorio, Agroenergia","Via Celoria 2 20133 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Oncologia ed Emato-Oncologia","Via Festa del Perdono 7 20122 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Scienze Biomediche e Cliniche L. Sacco","Via Giovanni Battista Grassi 74 20157 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Scienze Biomediche per la Salute","Via Mangiagalli 31 20133 Milano"))
    dipartimenti_unimi.append(("Dipartimento di Scienze Biomediche, Chirurgiche ed Odontoiatriche","Via della Commenda 10 20122 Milano"))
    #napoli
    dipartimenti_unina = list()
    dipartimenti_unina.append(("Dipartimento di Agraria","Via Università 100 - 80055 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Architettura","Via Monteoliveto 3 - 80134 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Biologia","Via Cupa Nuova Cintia 21 - 80126 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Economia, Management, Istituzioni","Via Cupa Nuova Cintia 21 - 80126 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Farmacia","Via Domenico Montesano 49 - 80131 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Fisica \"Ettore Pancini\"","Cupa Nuova Cintia, 21 - 80126 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Giurisprudenza","Via Nuova Marina, 33 - 80133 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Ingegneria Chimica, dei Materiali e della Produzione Industriale","Piazzale Tecchio, 80 - 80125 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Ingegneria Civile, Edile e Ambientale","Via Claudio, 21 - 80125 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Ingegneria Elettrica e delle Tecnologie dell Informazione","Via Claudio, 21 - 80125 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Ingegneria Industriale","Piazzale Tecchio, 80 - 80125 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Matematica e Applicazioni \"Renato Caccioppoli\"","Cupa Nuova Cintia, 21 - 80126 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Medicina Clinica e Chirurgia","Via Pansini, 5 - 80131 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Medicina Molecolare e Biotecnologie Mediche","Via Pansini, 5 - 80131 - Napoli "))
    dipartimenti_unina.append(("Dipartimento di Medicina Veterinaria e Produzioni Animali","Via Federico Delpino, 1 - 80137 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Neuroscienze e Scienze Riproduttive ed Odontostomatologiche","Via Pansini, 5 - 80131 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Sanità Pubblica","Via Pansini, 5 - 80131 - Napoli "))
    dipartimenti_unina.append(("Dipartimento di Scienze Biomediche Avanzate","Via Pansini, 5 - 80131 - Napoli "))
    dipartimenti_unina.append(("Dipartimento di Scienze Chimiche","Cupa Nuova Cintia, 21 - 80126 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Scienze della Terra, dell Ambiente e delle Risorse","Cupa Nuova Cintia, 21 - 80126 - Napoli - Edificio L "))
    dipartimenti_unina.append(("Dipartimento di Scienze Economiche e Statistiche","Cupa Nuova Cintia, 21 - 80126 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Scienze Mediche Traslazionali","Via Pansini, 5 - 80131 - Napoli "))
    dipartimenti_unina.append(("Dipartimento di Scienze Politiche","Via Leopoldo Rodinò, 22 - 80138 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Scienze Sociali","Vico Monte di Pietà, 1 - 80138 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Strutture per l Ingegneria e l Architettura","Piazzale Vincenzo Tecchio, 80 - 80125 - Napoli"))
    dipartimenti_unina.append(("Dipartimento di Studi Umanistici","Via Porta di Massa, 1 - 80133 - Napoli"))
    sql = database_connection("bdm_unipa")
    for dipartimento in dipartimenti_unipa:
        query = "INSERT INTO dipartimento(nome, indirizzo) VALUES("
        for value in dipartimento:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
        print(query[:-1] + ")")
    sql = database_connection("bdm_unimi")
    for dipartimento in dipartimenti_unimi:
        query = "INSERT INTO dipartimento(nome, indirizzo) VALUES("
        for value in dipartimento:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
        print(query[:-1] + ")")
    sql = database_connection("bdm_unina")
    for dipartimento in dipartimenti_unina:
        query = "INSERT INTO dipartimento(nome, indirizzo) VALUES("
        for value in dipartimento:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
        print(query[:-1] + ")")
    sql = database_connection("bdm_unito")
    for dipartimento in dipartimenti_unito:
        query = "INSERT INTO dipartimento(nome, indirizzo) VALUES("
        for value in dipartimento:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
        print(query[:-1] + ")")


creazione_dipartimenti()
