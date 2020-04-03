import datetime
import random
import numpy as np
import pandas as pd
from codicefiscale import codicefiscale


names = pd.read_csv("../res/datasets/nomi.csv")
surnames = pd.read_csv("../res/datasets/cognomi.csv")
hospitals = pd.read_csv("../res/datasets/ospedali.csv")
founds = pd.read_csv("../res/datasets/contributi_atenei.csv", sep=";")
prefisso_telefono_unipa = "091 238 "
prefisso_telefono_unito = "011 670 "
prefisso_telefono_unina = "081 420 "
prefisso_telefono_unimi = "091 03 "
livello_stipendio_qualifica = list()
livello_stipendio_qualifica.append(("B", 1050.45, "Titolo di studio di scuola d’obbligo"))
livello_stipendio_qualifica.append(("C", 1231.97, "Diploma di scuola superiore"))
livello_stipendio_qualifica.append(("D", 1767.81, "Diploma di laurea"))
livello_stipendio_qualifica.append(("EP", 2083.33, "Diploma di laurea e particolare qualificazione personale"))
tipologia_contratto_strutturato = list()
tipologia_contratto_strutturato.append("Professore ordinario")
tipologia_contratto_strutturato.append("Professore associato")
tipologia_contratto_strutturato.append("Ricercatore a tempo indeterminato")
tipologia_contratto_strutturato.append("Ricercatore a tempo determinato")
tipologia_contratto_non_strutturato = list()
tipologia_contratto_non_strutturato.append("Assegnista")
tipologia_contratto_non_strutturato.append("Dottorando")
tipologia_contratto_non_strutturato.append("Contrattista")

#GENERAZIONE PERSONALE
for i in range(0, 500):
    name = names.iloc[np.random.randint(0, 100), 0]
    surname = surnames.iloc[np.random.randint(0, 100), 0]
    day = np.random.randint(1, 32)
    month = np.random.randint(1, 13)
    year = np.random.randint(1950, 1995)
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(1992, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    date = str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")
    sex = ""
    if name[-1] == "A":
        sex = "F"
    else:
        sex = "M"
    city = hospitals.iloc[np.random.randint(0, len(hospitals)), 1]
    if city.find("/") > 0:
        city = city[:city.find("/")]
    codice_fiscale = codicefiscale.encode(surname=surname, name=name, sex=sex, birthdate=date, birthplace=city)
    telefono = prefisso_telefono_unipa
    #telefono = prefisso_telefono_unito
    #telefono = prefisso_telefono_unina
    #telefono = prefisso_telefono_unimi
    for _ in range(0, 4):
        telefono += str(np.random.randint(0, 10))
    stipendio = (2020 - int(date[:4])) * 6.34
    random_number = np.random.randint(1, 4)
    if random_number == 1:
        random_number = np.random.randint(1, 11)
        livello = ""
        qualifica = ""
        if random_number < 4:
            livello = livello_stipendio_qualifica[0][0]
            stipendio += livello_stipendio_qualifica[0][1]
            qualifica = livello_stipendio_qualifica[0][2]
        elif random_number < 8:
            livello = livello_stipendio_qualifica[1][0]
            stipendio += livello_stipendio_qualifica[1][1]
            qualifica = livello_stipendio_qualifica[1][2]
        elif random_number < 10:
            livello = livello_stipendio_qualifica[2][0]
            stipendio += livello_stipendio_qualifica[2][1]
            qualifica = livello_stipendio_qualifica[2][2]
        else:
            livello = livello_stipendio_qualifica[3][0]
            stipendio += livello_stipendio_qualifica[3][1]
            qualifica = livello_stipendio_qualifica[3][2]
    else:
        tipologia_contratto = ""
        stipendio = np.nan
        if random_number == 2:
            random_number = np.random.randint(1, 8)
            promozioni = list()
            if random_number < 2:
                tipologia_contratto = tipologia_contratto_strutturato[0]
                stipendio += 2550.72
                prima_promozione_anno_inizio = np.random.randint(1980, 2000)
                prima_promozione_anno_fine = np.random.randint(prima_promozione_anno_inizio, 2005)
                vecchio_stipendio = (prima_promozione_anno_fine - int(date[:4])) * 6.34 + 1478.11
                promozioni.append((str(prima_promozione_anno_inizio) + "/01/01", str(prima_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
                seconda_promozione_anno_inizio = np.random.randint(prima_promozione_anno_fine, 2010)
                seconda_promozione_anno_fine = np.random.randint(seconda_promozione_anno_inizio, 2015)
                vecchio_stipendio = (seconda_promozione_anno_fine - int(date[:4])) * 6.34 + 1802.89
                promozioni.append((str(seconda_promozione_anno_inizio) + "/01/01", str(seconda_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[2]))
                terza_promozione_anno_inizio = np.random.randint(seconda_promozione_anno_fine, 2018)
                terza_promozione_anno_fine = np.random.randint(terza_promozione_anno_inizio, 2019)
                vecchio_stipendio = (terza_promozione_anno_fine - int(date[:4])) * 6.34 + 2123.19
                promozioni.append((str(terza_promozione_anno_inizio) + "/01/01", str(terza_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[1]))
            elif random_number < 4:
                tipologia_contratto = tipologia_contratto_strutturato[1]
                stipendio += 2123.19
                prima_promozione_anno_inizio = np.random.randint(1990, 2010)
                prima_promozione_anno_fine = np.random.randint(prima_promozione_anno_inizio, 2015)
                vecchio_stipendio = (prima_promozione_anno_fine - int(date[:4])) * 6.34 + 1478.11
                promozioni.append((str(prima_promozione_anno_inizio) + "/01/01", str(prima_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
                seconda_promozione_anno_inizio = np.random.randint(prima_promozione_anno_fine, 2018)
                seconda_promozione_anno_fine = np.random.randint(seconda_promozione_anno_inizio, 2019)
                vecchio_stipendio = (seconda_promozione_anno_fine - int(date[:4])) * 6.34 + 1802.89
                promozioni.append((str(seconda_promozione_anno_inizio) + "/01/01", str(seconda_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[2]))
            elif random_number < 6:
                tipologia_contratto = tipologia_contratto_strutturato[2]
                stipendio += 1802.89
                anno_inizio = np.random.randint(2000, 2018)
                anno_fine = np.random.randint(anno_inizio, 2019)
                vecchio_stipendio = (anno_fine - int(date[:4])) * 6.34 + 1478.11
                promozioni.append((str(anno_inizio) + "/01/01", str(anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
            else:
                tipologia_contratto = tipologia_contratto_strutturato[3]
                stipendio += 1478.11
            print(promozioni)
            ufficio = np.random.randint(101, 300)
        else:
            laboratorio_riferimento = "Lab " + str(np.random.randint(1, 100))



#GENERAZIONE ATTIVITA' DIDATTICHE
"""
attivita = list()
attivita = list("Basi di Matematica")
attivita = list("Geometria")
attivita = list("Fisica I")
attivita = list("Biologia")
attivita = list("Informatica")
attivita = list("Logica")
attivita = list("Attività per l'inserimento nel mondo del lavoro")
attivita = list("Chimica")
"""




#GENERAZIONE DIPARTIMENTI
#ID_Dipartimento, Nome, indirizzo, FONDO
dipartimenti = list()
dipartimenti.append(("Dipartimento di Biotecnologie Molecolari e Scienze per la Salute","Via Nizza, 52, 10126, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Chimica", "Via Pietro Giuria, 7, 10125, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Culture, Politica e Società","Lungo Dora Siena, 100 A, 10153, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Economia e Statistica \"Cognetti de Martiis\"","Lungo Dora Siena, 100 A, 10153, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Filosofia e Scienze dell’Educazione","Via S. Ottavio, 20, 10124, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Fisica","Via P. Giuria, 1, 10125, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Giurisprudenza","Lungo Dora Siena, 100 A, 10153, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Informatica","Corso Svizzera, 185, 10149, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Lingue e Letterature straniere e Culture moderne","Complesso Aldo Moro - via Verdi, fronte civico 41 - Torino", 'FONDO'))
dipartimenti.append(("Dipartimento di Management","Corso Unione Sovietica, 218 Bis, 10134, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Matematica \"Giuseppe Peano\"","Via Carlo Alberto, 10, 10123, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Neuroscienze \"Rita Levi Montalcini\"","Via Cherasco, 15, 10126, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Oncologia","Regione Gonzole, 10, 10043, Orbassano, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Psicologia","Via Verdi, 10, 10124, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienza e Tecnologia del Farmaco","Via P. Giuria, 9, 10125, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze Agrarie, Forestali e Alimentari","Largo Paolo Braccini, 2, 10095, Grugliasco, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze Chirurgiche","Corso Dogliotti, 14, 10126, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze Cliniche e Biologiche","Regione Gonzole, 10, 10043, Orbassano, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze della Sanità Pubblica e Pediatriche","Piazza Polonia, 94, 10126, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze della Terra","Via Valperga Caluso, 35, 10125, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze della Vita e Biologia dei Sistemi","Via Accademia Albertina, 13, 10123, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze economico-sociali e matematico-statistiche","Corso Unione Sovietica, 218 Bis, 10134, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze Mediche","Corso Dogliotti, 14, 10126, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Scienze Veterinarie","Largo Paolo Braccini, 2, 10095, Grugliasco, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Studi Storici","Via S. Ottavio, 20, 10124, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento di Studi Umanistici","Via S. Ottavio, 20, 10124, Torino, TO", 'FONDO'))
dipartimenti.append(("Dipartimento Interateneo di Scienze, Progetto e Politiche del Territorio","Viale Mattioli, 39, 10125, Torino, TO", 'FONDO'))


#UNIPA
dipartimenti_unipa = list()
dipartimenti_unipa.append(("Architettura","Viale delle Scienze, Ed. 14", FONDO))
dipartimenti_unipa.append(("Biomedicina, Neuroscienze e Diagnostica avanzata","Via del Vespro, 129", FONDO))
dipartimenti_unipa.append(("Culture e Società","Viale delle Scienze, Ed. 15", FONDO))
dipartimenti_unipa.append(("Discipline Chirurgiche, Oncologiche e Stomatologiche","Via Liborio Giuffrè, 5", FONDO))
dipartimenti_unipa.append(("Fisica e Chimica - Emilio Segrè","Viale delle Scienze, Ed. 17", FONDO))
dipartimenti_unipa.append(("Giurisprudenza","Via Maqueda, 172", FONDO))
dipartimenti_unipa.append(("Ingegneria","Viale delle Scienze, Ed. 8", FONDO))
dipartimenti_unipa.append(("Matematica e Informatica","Via Archirafi, 34", FONDO))
dipartimenti_unipa.append(("Promozione della Salute, Materno-Infantile, di Medicina Interna e Specialistica di Eccellenza \“G. D’Alessandro\”","Piazza delle Cliniche, 2", FONDO))
dipartimenti_unipa.append(("Scienze Agrarie, Alimentari e Forestali","Viale delle Scienze, Ed. 4", FONDO))
dipartimenti_unipa.append(("Scienze della Terra e del Mare","Via Archirafi, 22", FONDO))
dipartimenti_unipa.append(("Scienze e Tecnologie Biologiche Chimiche e Farmaceutiche","Viale delle Scienze, Ed. 16", FONDO))
dipartimenti_unipa.append(("Scienze Economiche, Aziendali e Statistiche","Viale delle Scienze, Ed. 13", FONDO))
dipartimenti_unipa.append(("Scienze Politiche e delle relazioni internazionali","Via Maqueda, 324", FONDO))
dipartimenti_unipa.append(("Scienze Psicologiche, Pedagogiche, dell’Esercizio Fisico e della Formazione","Viale delle Scienze, Ed. 15", FONDO))
dipartimenti_unipa.append(("Scienze Umanistiche","Viale delle Scienze, Ed. 12", FONDO))

#milano
dipartimenti_unimi = list()
dipartimenti_unimi.append(("Dipartimento di Beni Culturali e Ambientali","Via Festa del Perdono 720122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Bioscienze","Via Celoria 26 20133 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Biotecnologie Mediche e Medicina Traslazionale","Via Vanvitelli 32 20133 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Chimica","Via Golgi 19 20133 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Diritto Privato e Storia del Diritto","Via Festa del Perdono 7 20122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Diritto Pubblico Italiano e Sovranazionale","Via Festa del Perdono 7 20122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Economia, Management e Metodi Quantitativi","Via Conservatorio 7 20122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Filosofia Piero Martinetti","Via Festa del Perdono 7 20122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Fisiopatologia Medico-Chirurgica e dei Trapianti","Via Francesco Sforza 35 20122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Fisica Aldo Pontremoli","Via Celoria 16 20133 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Informatica Giovanni degli Antoni","Via Celoria 18 20135 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Lingue e Letterature Straniere","Piazza Sant'Alessandro 1 20122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Matematica Federigo Enriques","Via Saldini 50 20129 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Medicina Veterinaria","Lodi - Via dell'Università 6 26900 Lodi", FONDO))
dipartimenti_unimi.append(("Dipartimento di Scienze Agrarie e Ambientali - Produzione, Territorio, Agroenergia","Via Celoria 2 20133 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Oncologia ed Emato-Oncologia","Via Festa del Perdono 7 20122 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Scienze Biomediche e Cliniche L. Sacco","Via Giovanni Battista Grassi 74 20157 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Scienze Biomediche per la Salute","Via Mangiagalli 31 20133 Milano", FONDO))
dipartimenti_unimi.append(("Dipartimento di Scienze Biomediche, Chirurgiche ed Odontoiatriche","Via della Commenda 10 20122 Milano", FONDO))


#GENERAZIONE ENTI
#nome, descriizoni, livello, indirizzo, DA CHIEDERE COS'è IL LIVELLO AAAAAAAAAAAAAAAAAAH
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
enti_napoli.append(("Citta' Metropolitana di Napoli","www.cittametropolitana.na.it","","Piazza Matteotti, 1 - 80133 Napoli (NA)"))
enti_napoli.append(("Ente Provinciale per il Turismo di Napoli","www.eptnapoli.info","","CENTRO DIREZIONALE ISOLA C5 - 80121 Napoli (NA)"))
enti_napoli.append(("Istituto per le Tecnologie della Costruzione - ITC - Sede Secondaria Napoli","https://www.itc.cnr.it/home/chi-siamo/","","c/o Dist Federico II - via Claudio 21 - 80125 Napoli (NA)"))
enti_napoli.append(("Ordine degli Ingegneri della Provincia di Napoli","www.ordineingegnerinapoli.com","","Via Del Chiostro, 9 - 80134 Napoli (NA)"))
enti_napoli.append(("Sistema Ambiente Provincia di Napoli S.P.A.","www.sapnapoli.it","","Piazza Matteotti, 1 - 80133 Napoli (NA)"))
enti_napoli.append(("Ambito Territoriale Ottimale Napoli 3","www.atonapoli3.it","","Via Roma, 5 - 80032 Casamarciano (NA"))
enti_napoli.append(("Azienda Sanitaria Locale Napoli 2 Nord","www.aslnapoli2nord.it","","Via M. Lupoli,27 - 80027 Frattamaggiore (NA)"))
enti_milano.append(("Agenzia di Tutela della Salute della Citta' Metropolitana di Milano","www.ats-milano.it","","Corso Italia, 19 - 20122 Milano (MI)"))
enti_milano.append(("Biblioteca Braidense di Milano","http://www.braidense.it/","","Via Brera, 28 - 20121 Milano (MI)"))
enti_milano.append(("Citta' Metropolitana di Milano","www.cittametropolitana.mi.it","","Via Vivaio 1 - 20122 Milano (MI)"))
enti_milano.append(("Comune di Milano","www.comune.milano.it","","Piazza Della Scala, 2 - 20121 Milano (MI)"))
enti_milano.append(("Fondazione Teatro alla Scala di Milano","www.teatroallascala.org","","Via Filodrammatici 2 - 20121 Milano (MI)"))
enti_milano.append(("Milano Ristorazione","www.milanoristorazione.it","","Via Bernardo Quaranta, 41 - 20139 Milano (MI)"))
enti_milano.append(("Ordine Degli Avvocati di Milano","www.ordineavvocatimilano.it","","Via Carlo Freguglia, 1 - 20122 Milano (MI)"))
enti_milano.append(("Parco Nord Milano","www.parconord.milano.it","","Via Clerici, 150 - 20099 Sesto San Giovanni (MI)"))
enti_milano.append(("Ufficio d'Ambito della Citta' Metropolitana di Milano - Azienda Speciale","www.atocittametropolitanadimilano.it","","Viale Piceno, 60 - 20129 Milano (MI)"))


# GENERAZIONE FONDI
# nome budget ente
fondi_palermo = list()
fondi_torino = list()
fondi_napoli = list()
fondi_milano = list()

for i in range(0,11):
    fondi_torino.append((founds.iloc[i, 4], founds.iloc[i, 5]), 'ENTE')
    fondi_milano.append((founds.iloc[11+i, 4], founds.iloc[11+i, 5]), 'ENTE')
    fondi_napoli.append((founds.iloc[22+i, 4], founds.iloc[22+i, 5]), 'ENTE')
    fondi_palermo.append((founds.iloc[33+i, 4], founds.iloc[33+i, 5]), 'ENTE')
