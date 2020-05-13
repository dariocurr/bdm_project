from database_connection import database_connection
import datetime
import random
import math
from faker import Faker
import re

fake = Faker('it_IT')

sql = database_connection("bdm_unito") #bdm_unipa, bdm_unimi, bdm_unina
progetti = sql.execute_query("select * from progetto_ricerca")
aree = sql.execute_query("select * from area_ricerca")
dipartimenti = sql.execute_query("select id_dipartimento, nome  from dipartimento")
keywords = dict()

tipo = list()
tipo.append("Seminario")
tipo.append("Workshop")
tipo.append("Convegno")
tipo.append("Scuola di dottorato")
tipo.append("Summer school")

argomenti = dict()

def crea_argomenti_dipartimenti():
    argomenti['Dipartimento di Lingue e Letterature straniere e Culture moderne'] = ["Teologia", "Storia", "Storia delle religioni",
    "Beni culturali", "Linguistica", "Lingue e letterature classiche", "Discipline dell'arte, musica e spettacolo",
    "Archeologia", "Filosofia", "Storia delle lettere italiane"]

    argomenti['Dipartimento di Filosofia e Scienze dell’Educazione'] = ["Teologia", "Storia", "Storia delle religioni",
    "Beni culturali", "Linguistica inglese", "Lingue e letterature spagnole", "Discipline dell'arte, musica e spettacolo",
    "Archeologia", "Filosofia", "Storia delle lettere inglesi"]

    argomenti['Dipartimento di Psicologia'] = ["Percezione",
    "Attenzione","Intelligenza","Memoria","Pensiero","Coscienza","Emozione","Personalità",
    "Conoscere la psiche","Ontologia newtoniana"]

    argomenti['Dipartimento di Studi Storici'] = ["discipline giuspubblicistiche",
    "economia politica e politica economica","scienza delle finanze e contabilità pubblica",
    "sociologia e metodologia della ricerca sociale","storia delle dottrine politiche","storia delle istituzioni politiche",
    "filosofia politica e altre branche della filosofia","statistica e demografia","scienza politica","relazioni internazionali"]

    argomenti['Dipartimento di Culture, Politica e Societa'] = ["discipline giuspubblicistiche",
    "economia politica e politica economica","scienza delle finanze e contabilità pubblica",
    "sociologia e metodologia della ricerca sociale","storia delle dottrine politiche","storia delle istituzioni politiche",
    "filosofia politica e altre branche della filosofia","statistica e demografia","scienza politica","relazioni internazionali"]

    argomenti['Dipartimento di Scienze economico-sociali e matematico-statistiche'] = ["Tecnologia dei cicli produttivi","Storia del pensiero economico",
    "Management della sostenibilità e dell'innovazione","Revisione aziendale","Economia e Finanza Internazionale",
    "Diritto commerciale - mercati globali","Economia e gestione delle imprese internazionali","Corporate Finance",
    "Filosofia della scienza, economia e digitalizzazione","Teoria delle reti e delle decisioni"]

    argomenti['Dipartimento di Economia e Statistica Cognetti de Martiis'] = ["Tecnologia dei cicli produttivi","Storia del pensiero economico",
    "Management della sostenibilità e dell'innovazione","Revisione aziendale","Economia e Finanza Internazionale",
    "Diritto commerciale - mercati globali","Economia e gestione delle imprese internazionali","Corporate Finance",
    "Filosofia della scienza, economia e digitalizzazione","Teoria delle reti e delle decisioni"]

    argomenti['Dipartimento di Management'] = ["Tecnologia dei cicli produttivi","Storia del pensiero economico",
    "Management della sostenibilità e dell'innovazione","Revisione aziendale","Economia e Finanza Internazionale",
    "Diritto commerciale - mercati globali","Economia e gestione delle imprese internazionali","Corporate Finance",
    "Filosofia della scienza, economia e digitalizzazione","Teoria delle reti e delle decisioni"]

    argomenti['Dipartimento di Scienze Agrarie, Forestali e Alimentari'] = ["agronomia", "estimo", "diritto agrario",
    "costruzioni", "idraulica", "tecnologie alimentari", "industrie agrarie", "zootecnica", "zoologia",
    "nutrizione", "entomologia"]

    argomenti['Dipartimento di Scienze della Terra'] = ["Tafonomia","Evoluzione e paleontologia",
    "Stratigrafia e biostratigrafia","Faune insulari","Sistematica di gruppi animali",
    "Degradazione meteorica delle rocce","Azione erosiva delle acque superficiali","Processi di versante",
    "Dinamica fluviale","Dinamica costiera"]

    argomenti['Dipartimento di Scienze della Vita e Biologia dei Sistemi'] = ["Tafonomia","Evoluzione e paleontologia",
    "Stratigrafia e biostratigrafia","Faune insulari","Sistematica di gruppi animali",
    "Degradazione meteorica delle rocce","Azione erosiva delle acque superficiali","Processi di versante",
    "Dinamica fluviale","Dinamica costiera"]

    argomenti['Dipartimento di Informatica'] = ["Gruppi nilpotenti finiti","Gruppi abeliani finitamente generati",
    "Curve razionali. Teorema di Luroth","Teorema fondamentale della Geometria proiettiva","Le geometrie non euclidee di tipo ellittico: proprietà e modelli",
    "Equazioni di terzo grado e trisezione dell’angolo: metodologie e costruzioni","Data mining","Algoritmi efficienti su grafi","Cybersecurity","Smart cities"]

    argomenti['Dipartimento di Matematica "Giuseppe Peano"'] = ["Gruppi nilpotenti finiti","Gruppi abeliani finitamente generati",
    "Curve razionali. Teorema di Luroth","Teorema fondamentale della Geometria proiettiva","Le geometrie non euclidee di tipo ellittico: proprietà e modelli",
    "Equazioni di terzo grado e trisezione dell’angolo: metodologie e costruzioni","Data mining","Algoritmi efficienti su grafi","Cybersecurity","Smart cities"]

    argomenti['Dipartimento di Ingegneria Chimica, dei Materiali e della Produzione Industriale'] = ["Azionamento elettrico","Compatibilità elettromagnetica","Distribuzione di energia elettrica",
    "Macchine elettriche","Misure elettriche","Produzione di energia elettrica","Trasporto di energia elettrica","Load flow","Elettronica di potenza",
    "Circuiti integrati"]

    argomenti['Dipartimento di Ingegneria Civile, Edile e Ambientale'] = ["Azionamento elettrico","Compatibilità elettromagnetica","Distribuzione di energia elettrica",
    "Macchine elettriche","Misure elettriche","Produzione di energia elettrica","Trasporto di energia elettrica","Load flow","Elettronica di potenza",
    "Circuiti integrati"]

    argomenti['Dipartimento di Ingegneria Elettrica e delle Tecnologie dell Informazione'] = ["Azionamento elettrico","Compatibilità elettromagnetica","Distribuzione di energia elettrica",
    "Macchine elettriche","Misure elettriche","Produzione di energia elettrica","Trasporto di energia elettrica","Load flow","Elettronica di potenza",
    "Circuiti integrati"]

    argomenti['Dipartimento di Ingegneria Industriale'] = ["Azionamento elettrico","Compatibilità elettromagnetica","Distribuzione di energia elettrica",
    "Macchine elettriche","Misure elettriche","Produzione di energia elettrica","Trasporto di energia elettrica","Load flow","Elettronica di potenza",
    "Circuiti integrati"]

    argomenti['Dipartimento di Giurisprudenza'] = ["Diritto costituzionale","filosofia del diritto","Inglese giuridico",
    "Diritto romano","diritto costituzionale","filosofia del diritto","Diritto agrario","Diritto commerciale",
    "Diritto del lavoro","Diritto dell'economia"]

    argomenti['Dipartimento di Diritto Privato e Storia del Diritto'] = ["Diritto costituzionale","filosofia del diritto","Inglese giuridico",
    "Diritto romano","diritto costituzionale","filosofia del diritto","Diritto agrario","Diritto commerciale",
    "Diritto del lavoro","Diritto dell'economia"]

    argomenti['Dipartimento di Architettura'] = ["supporto tecnologico e materiali per il restauro","applicazione di nanotecnologie ai beni culturali",
    "strategie di sviluppo in ambito mediterraneo","strategie per la competitività dei sistemi produttivi",
    "teoria e metodi del progetto di architettura, città e paesaggio","strategie e forme delle modificazioni urbane",
    "accessibilità e mobilità: nuovi spazi pubblici e infrastrutture","strategie e sistemi di paesaggio",
    "sperimentazioni progettuali sulla città: aree dismesse e di margine","processi innovativi di trasformazione degli spazi pubblici urbani, attraverso tecniche digitali",
    "exibit e installazioni nella città contemporanea"]

    argomenti['Dipartimento di Strutture per l Ingegneria e l Architettura'] = ["supporto tecnologico e materiali per il restauro","applicazione di nanotecnologie ai beni culturali",
    "strategie di sviluppo in ambito mediterraneo","strategie per la competitività dei sistemi produttivi",
    "teoria e metodi del progetto di architettura, città e paesaggio","strategie e forme delle modificazioni urbane",
    "accessibilità e mobilità: nuovi spazi pubblici e infrastrutture","strategie e sistemi di paesaggio",
    "sperimentazioni progettuali sulla città: aree dismesse e di margine","processi innovativi di trasformazione degli spazi pubblici urbani, attraverso tecniche digitali",
    "exibit e installazioni nella città contemporanea"]

    argomenti['Dipartimento di Beni Culturali e Ambientali'] = ["Cinema e media","Semiotica","Sociologia del giornalismo",
    "Storia dell'arte","Filosofia sociale","Sociologia dei media digitali","Sociologia dell'amministrazione",
    "Statistica sociale","Marketing","Comunicazione"]

    argomenti['Dipartimento di Fisica'] = ["Anatomia e istologia apparato oculare",
    "Informatica","Ottica Geometrica","Chimica inorganica","chimica supramolecolare",
    "Sostanze naturali","Fisica statistica","Meccanica quantistica","Spettroscopia","Radiazioni"]

    argomenti['Dipartimento di Chimica'] = ["Anatomia e istologia apparato oculare",
    "Informatica","Ottica Geometrica","Chimica inorganica","chimica supramolecolare",
    "Sostanze naturali","Fisica statistica","Meccanica quantistica","Spettroscopia","Radiazioni"]

    argomenti['Dipartimento di Scienze Cliniche e Biologiche'] = ["Metodologie proteomiche","Epigenetica",
    "Neurobiologia molecolare","Immunologia","Fisiologia","Patologia","Anatomia","Psichiatria",
    "Riabilitazione Psichiatrica","Medicina legale"]

    argomenti['Dipartimento di Neuroscienze "Rita Levi Montalcini"'] = ["Metodologie proteomiche","Epigenetica",
    "Neurobiologia molecolare","Immunologia","Fisiologia","Patologia","Anatomia","Psichiatria",
    "Riabilitazione Psichiatrica","Medicina legale"]

    argomenti['Dipartimento di Scienza e Tecnologia del Farmaco'] = ["Chimica generale","Chimica inorganica","Biologia animale","Biochimica",
    "Sicurezza nei laboratori","Chimica analitica","Dinamica molecolare",
    "Igiene","Chimica analitica","Scienze dell'alimentazione"]

    argomenti['Dipartimento di Scienze Chirurgiche'] = ["Chimica generale","Chimica inorganica","Biologia animale","Biochimica",
    "Sicurezza nei laboratori","Chimica analitica","Dinamica molecolare",
    "Igiene","Chimica analitica","Scienze dell'alimentazione"]

    argomenti['Dipartimento di Biotecnologie Molecolari e Scienze per la Salute'] =  ["Istologia",
    "Psicologia clinica","Assistenza al parto","Ginecologia","Dermatologia","Scienze biomediche",
    "Produzione degli alimenti","Scienze dietetiche","Infermieristica","Neurologia"]

    argomenti['Dipartimento di Scienze Veterinarie'] = ["Radioterapia",
    "Istologia","Malattie dei tessuti dentali","Paradontologia","Biochimica","Anatomia","Igiene",
    "Farmacologia","Gastroenterologia","Malattie infettive"]

    argomenti['Dipartimento di Oncologia'] = ["Radioterapia",
    "Istologia","Malattie dei tessuti dentali","Paradontologia","Biochimica","Anatomia","Igiene",
    "Farmacologia","Gastroenterologia","Malattie infettive"]

    argomenti['Dipartimento di Scienze della Sanità Pubblica e Pediatriche'] = ["Radioterapia",
    "Istologia","Malattie dei tessuti dentali","Paradontologia","Biochimica","Anatomia","Igiene",
    "Farmacologia","Gastroenterologia","Malattie infettive"]

    argomenti['Dipartimento di Scienze Mediche'] = ["Istologia",
    "Psicologia clinica","Assistenza al parto","Ginecologia","Dermatologia","Scienze biomediche",
    "Produzione degli alimenti","Scienze dietetiche","Infermieristica","Neurologia"]


def area_from_dipartimento(name):
    if name == 'Dipartimento di Psicologia' or name == 'Dipartimento di Culture, Politica e Societa' or name == 'Dipartimento di Lingue e Letterature straniere e Culture moderne' or name == 'Dipartimento di Filosofia e Scienze dell’Educazione' or name == 'Dipartimento di Studi Storici' or name == 'Dipartimento di Giurisprudenza' or name == 'Dipartimento di Diritto Privato e Storia del Diritto':
        return 11
    elif name == 'Dipartimento di Management' or name == 'Dipartimento di Economia e Statistica Cognetti de Martiis' or name == 'Dipartimento di Scienze economico-sociali e matematico-statistiche':
        return 10
    elif name == 'Dipartimento di Scienze Agrarie, Forestali e Alimentari' or name == 'Dipartimento di Scienze Cliniche e Biologiche':
        return 1
    elif name == 'Dipartimento di Scienze della Terra' or name == 'Dipartimento di Scienze della Vita e Biologia dei Sistemi':
        return 12
    elif name == 'Dipartimento di Matematica "Giuseppe Peano"':
        return 4
    elif name == 'Dipartimento di Informatica':
        r = random.randint(0,1)
        if r == 0:
            return 14
        else:
            return 2
    elif name == 'Dipartimento di Ingegneria Chimica, dei Materiali e della Produzione Industriale' or name == 'Dipartimento di Ingegneria Elettrica e delle Tecnologie dell Informazione' or name == 'Dipartimento di Ingegneria Industriale' or name == 'Dipartimento di Ingegneria Civile, Edile e Ambientale':
        return 7
    elif name == 'Scienze Politiche e delle relazioni internazionali':
        return 13
    elif name == 'Dipartimento di Beni Culturali e Ambientali' or name == 'Dipartimento di Architettura':
        return 9
    elif name == 'Dipartimento di Fisica':
        return 5
    elif name == 'Dipartimento di Chimica' or name == 'Dipartimento di Scienza e Tecnologia del Farmaco':
        return 6
    elif name == 'Dipartimento di Scienze Chirurgiche' or name == 'Dipartimento di Biotecnologie Molecolari e Scienze per la Salute' or name == 'Dipartimento di Scienze Veterinarie' or name == 'Dipartimento di Oncologia' or name == 'Dipartimento di Scienze Mediche' or name == 'Dipartimento di Scienze della Sanità Pubblica e Pediatriche' or name == 'Dipartimento di Neuroscienze "Rita Levi Montalcini"':
        return 3


def get_random_argomento_from_dipartimento(nome):
    r = random.randint(0,9)
    return argomenti[nome][r]


def data_random(anno_min, anno_max):
    start_date = datetime.date(anno_min, 1, 1)
    end_date = datetime.date(anno_max, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return str(start_date + datetime.timedelta(days=random_number_of_days)).replace("-", "/")


def get_random_dipartimento():
    index = random.randint(0,24)
    return dipartimenti[index]


def get_random_portata(tipo):
    if tipo == 0:
        return random.randint(50,150)
    elif tipo == 1:
        return random.randint(20,50)
    elif tipo == 2:
        return random.randint(100,300)
    elif tipo == 3:
        return random.randint(5,10)
    elif tipo == 4:
        return random.randint(15,50)


def get_random_durata(tipo):
    if tipo == 0:
        return 1
    elif tipo == 1:
        return random.randint(1,3)
    elif tipo == 2:
        return random.randint(1,5)
    elif tipo == 3:
        return random.randint(15,60)
    elif tipo == 4:
        return random.randint(3,7)


def get_random_progetto_ricerca(id):
    index = random.randrange(len(progetti))
    for progetto in progetti:
        if id == progetto[6]:
            return progetti[index][0]


def creazione_eventi():
    crea_argomenti_dipartimenti()
    ran = random.randint(1000,2000)
    for i in range(0, ran):
        index_tipo = random.randint(0,4)
        durata = get_random_durata(index_tipo)
        portata = get_random_portata(index_tipo)
        partitecipanti_previsti = portata - (random.randint(0,math.floor(portata/2)))
        partitecipanti_effettivi = partitecipanti_previsti - (random.randint(0,math.floor(partitecipanti_previsti/3)))
        dipartimento = get_random_dipartimento()
        pubblicazione = (get_random_argomento_from_dipartimento(dipartimento[1]).replace("'", " "),
                        tipo[index_tipo],
                        data_random(2000, 2020),
                        durata,
                        portata,
                        fake.address().replace("'", " "),
                        partitecipanti_previsti,
                        partitecipanti_effettivi,
                        partitecipanti_effettivi*random.randint(5,10),
                        get_random_progetto_ricerca(area_from_dipartimento(dipartimento[1])),
                        dipartimento[0]
                        )
        query = "INSERT INTO evento(argomento, tipo, data, durata, portata, luogo_evento, partitecipanti_previsti, partitecipanti_effettivi, ricavo, progetto_ricerca, dipartimento) VALUES ("
        for value in pubblicazione:
            query += "'" + str(value) + "',"
        print(query[:-1] + ")")
        sql.execute_query(query[:-1] + ")")


creazione_eventi()
