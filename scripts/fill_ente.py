from database_connection import database_connection

def creazione_enti():
    #nome, descriizoni, livello, indirizzo
    enti_palermo = list()
    enti_torino = list()
    enti_napoli = list()
    enti_milano = list()
    enti_palermo.append(("Azienda Sanitaria Provinciale di Palermo","","","Via Giacomo Gusmano, 24 - 90141 Palermo (PA)"))
    enti_palermo.append(("Consorzio Universitario della Provincia di Palermo","http://www.consunipa.it/wordpress/ente/mission/","","Via Maqueda 100 - 90100 Palermo (PA)" ))
    enti_palermo.append(("Consorzio Area Sviluppo Industriale Palermo","http://www.irsapsicilia.it/index.php?option=com_content&view=article&id=380&Itemid=684","","Via Enrico Ferruzza, 5 - 90124 Palermo (PA)"))
    enti_palermo.append(("Ersu Palermo","www.ersupalermo.it","","Viale Delle Scienze, Edificio 1 - 90128 Palermo (PA)"))
    enti_palermo.append(("Consiglio Nazionale delle Ricerche - CNR","www.cnr.it","","Piazzale Aldo Moro, 7 - 00185 Roma (RM)"))
    enti_palermo.append(("Ordine degli Ingegneri della Provincia di Palermo","www.ingpa.com","","Via Francesco Crispi, 120 - 90139 Palermo (PA)"))
    enti_palermo.append(("Ordine dei Farmacisti della Provincia di Palermo","www.ordinefarmacistipalermo.it","","Via Mariano Stabile N. 118/B - 90139 Palermo (PA)"))
    enti_palermo.append(("SISPI - SISTEMA PALERMO INNOVAZIONE S.P.A.","www.sispi.it","","Via A.s.denti Di Piraino, 7 - 90142 Palermo (PA)"))
    enti_palermo.append(("Teatro Biondo Stabile di Palermo","www.teatrobiondo.it","","Via Teatro Biondo, 11 - 90133 Palermo (PA)"))
    enti_palermo.append(("Comune di Palermo","www.comune.palermo.it","","Piazza Pretoria, 1 - Palazzo Delle Aquile - 90133 Palermo (PA)"))
    enti_torino.append(("Afc Torino S.P.A.","www.cimiteritorino.it","","Corso Peschiera, 193 - 10141 Torino (TO)"))
    enti_torino.append(("Azienda Ospedaliera Ordine Mauriziano di Torino","www.mauriziano.it","","Via Magellano, 1 - 10128 Torino (TO)"))
    enti_torino.append(("Biblioteca nazionale di Torino","http://www.bnto.librari.beniculturali.it/","","Piazza carlo Albeerto, 3 - 10123 Torino (TO)"))
    enti_torino.append(("Collegio dei Geometri e Geometri Laureati di Torino e Provincia","https://collegiogeometri.to.it/","","Via Toselli 1 - 10129 Torino (TO)"))
    enti_torino.append(("Turismo Torino e Provincia S.C.R.L","www.turismotorino.org","","Via Maria Vittoria, 19 - 10123 Torino (TO)"))
    enti_torino.append(("Sede Torino Protocollo","http://www.comune.torino.it/circ1/cm/pages/ServeBLOB.php/L/IT/IDPagina/1592","","Via Pio VII, 9 - 10135 Torino (TO)"))
    enti_torino.append(("RTS Torino","http://www.rgs.mef.gov.it/VERSIONE-I/sistema_delle_ragionerie/ragionerie_territoriali_dello_stato/sportelli_rts/piemonte/rts_torino_aosta/","","Corso Bolzano, 44 - 10121 Torino (TO)"))
    enti_napoli.append(("Accademia Belle Arti di Napoli","www.accademiadinapoli.it","","Via Vincenzo Bellini, 36 - 80138 Napoli (NA)"))
    enti_napoli.append(("Azienda Sanitaria Locale di Napoli 3 Sud","www.aslnapoli3sud.it","","Via Marconi 66 - 80059 Torre del Greco (NA)"))
    enti_napoli.append(("Camera di Commercio, Industria, Artigianato e Agricoltura di Napoli","www.na.camcom.gov.it","","Via S. Aspreno 2 - 80133 Napoli (NA)"))
    enti_napoli.append(("Citta Metropolitana di Napoli","www.cittametropolitana.na.it","","Piazza Matteotti, 1 - 80133 Napoli (NA)"))
    enti_napoli.append(("Ente Provinciale per il Turismo di Napoli","www.eptnapoli.info","","CENTRO DIREZIONALE ISOLA C5 - 80121 Napoli (NA)"))
    enti_napoli.append(("Istituto per le Tecnologie della Costruzione - ITC - Sede Secondaria Napoli","https://www.itc.cnr.it/home/chi-siamo/","","c/o Dist Federico II - via Claudio 21 - 80125 Napoli (NA)"))
    enti_napoli.append(("Ordine degli Ingegneri della Provincia di Napoli","www.ordineingegnerinapoli.com","","Via Del Chiostro, 9 - 80134 Napoli (NA)"))
    enti_napoli.append(("Sistema Ambiente Provincia di Napoli S.P.A.","www.sapnapoli.it","","Piazza Matteotti, 1 - 80133 Napoli (NA)"))
    enti_napoli.append(("Ambito Territoriale Ottimale Napoli 3","www.atonapoli3.it","","Via Roma, 5 - 80032 Casamarciano (NA"))
    enti_napoli.append(("Azienda Sanitaria Locale Napoli 2 Nord","www.aslnapoli2nord.it","","Via M. Lupoli,27 - 80027 Frattamaggiore (NA)"))
    enti_milano.append(("Biblioteca Braidense di Milano","http://www.braidense.it/","","Via Brera, 28 - 20121 Milano (MI)"))
    enti_milano.append(("Comune di Milano","www.comune.milano.it","","Piazza Della Scala, 2 - 20121 Milano (MI)"))
    enti_milano.append(("Fondazione Teatro alla Scala di Milano","www.teatroallascala.org","","Via Filodrammatici 2 - 20121 Milano (MI)"))
    enti_milano.append(("Milano Ristorazione","www.milanoristorazione.it","","Via Bernardo Quaranta, 41 - 20139 Milano (MI)"))
    enti_milano.append(("Ordine Degli Avvocati di Milano","www.ordineavvocatimilano.it","","Via Carlo Freguglia, 1 - 20122 Milano (MI)"))
    enti_milano.append(("Parco Nord Milano","www.parconord.milano.it","","Via Clerici, 150 - 20099 Sesto San Giovanni (MI)"))
    enti_milano.append(("Ufficio Ambito della Citta Metropolitana di Milano - Azienda Speciale","www.atocittametropolitanadimilano.it","","Viale Piceno, 60 - 20129 Milano (MI)"))
    sql = database_connection("bdm_unipa")
    for ente in enti_palermo:
        query = "INSERT INTO ente(nome, descrizione, livello, indirizzo) VALUES ("
        for value in ente:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    sql = database_connection("bdm_unimi")
    for ente in enti_milano:
        query = "INSERT INTO ente(nome, descrizione, livello, indirizzo) VALUES ("
        for value in ente:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    sql = database_connection("bdm_unina")
    for ente in enti_napoli:
        query = "INSERT INTO ente(nome, descrizione, livello, indirizzo) VALUES ("
        for value in ente:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
    sql = database_connection("bdm_unito")
    for ente in enti_torino:
        query = "INSERT INTO ente(nome, descrizione, livello, indirizzo) VALUES ("
        for value in ente:
            query += "'" + str(value) + "',"
        sql.execute_query(query[:-1] + ")")
