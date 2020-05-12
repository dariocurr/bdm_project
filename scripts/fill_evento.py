from database_connection import database_connection
import datetime
import random
import math
from faker import Faker
import re

fake = Faker('it_IT')

sql = database_connection("bdm_unipa") #bdm_unipa, bdm_unimi, bdm_unina
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
    argomenti['Scienze Umanistiche'] = ["Teologia", "Storia", "Storia delle religioni",
    "Beni culturali", "Linguistica", "Lingue e letterature classiche", "Discipline dell'arte, musica e spettacolo",
    "Archeologia", "Filosofia", "Storia delle lettere italiane"]
    argomenti['Scienze Psicologiche, Pedagogiche, dell’Esercizio Fisico e della Formazione'] = ["Percezione",
    "Attenzione","Intelligenza","Memoria","Pensiero","Coscienza","Emozione","Personalità",
    "Conoscere la psiche","Ontologia newtoniana"]
    argomenti['Scienze Politiche e delle relazioni internazionali'] = ["discipline giuspubblicistiche",
    "economia politica e politica economica","scienza delle finanze e contabilità pubblica",
    "sociologia e metodologia della ricerca sociale","storia delle dottrine politiche","storia delle istituzioni politiche",
    "filosofia politica e altre branche della filosofia","statistica e demografia","scienza politica","relazioni internazionali"]
    argomenti['Scienze Economiche, Aziendali e Statistiche'] = ["Tecnologia dei cicli produttivi","Storia del pensiero economico",
    "Management della sostenibilità e dell'innovazione","Revisione aziendale","Economia e Finanza Internazionale",
    "Diritto commerciale - mercati globali","Economia e gestione delle imprese internazionali","Corporate Finance",
    "Filosofia della scienza, economia e digitalizzazione","Teoria delle reti e delle decisioni"]
    argomenti['Scienze Agrarie, Alimentari e Forestali'] = ["agronomia", "estimo", "diritto agrario",
    "costruzioni", "idraulica", "tecnologie alimentari", "industrie agrarie", "zootecnica", "zoologia",
    "nutrizione", "entomologia"]
    argomenti['Scienze della Terra e del Mare'] = ["Tafonomia","Evoluzione e paleontologia",
    "Stratigrafia e biostratigrafia","Faune insulari","Sistematica di gruppi animali",
    "Degradazione meteorica delle rocce","Azione erosiva delle acque superficiali","Processi di versante",
    "Dinamica fluviale","Dinamica costiera"]
    argomenti['Matematica e Informatica'] = ["Gruppi nilpotenti finiti","Gruppi abeliani finitamente generati",
    "Curve razionali. Teorema di Luroth","Teorema fondamentale della Geometria proiettiva","Le geometrie non euclidee di tipo ellittico: proprietà e modelli",
    "Equazioni di terzo grado e trisezione dell’angolo: metodologie e costruzioni","Data mining","Algoritmi efficienti su grafi","Cybersecurity","Smart cities"]
    argomenti['Ingegneria'] = ["Azionamento elettrico","Compatibilità elettromagnetica","Distribuzione di energia elettrica",
    "Macchine elettriche","Misure elettriche","Produzione di energia elettrica","Trasporto di energia elettrica","Load flow","Elettronica di potenza",
    "Circuiti integrati"]
    argomenti['Giurisprudenza'] = ["Diritto costituzionale","filosofia del diritto","Inglese giuridico",
    "Diritto romano","diritto costituzionale","filosofia del diritto","Diritto agrario","Diritto commerciale",
    "Diritto del lavoro","Diritto dell'economia"]
    argomenti['Architettura'] = ["supporto tecnologico e materiali per il restauro","applicazione di nanotecnologie ai beni culturali",
    "strategie di sviluppo in ambito mediterraneo","strategie per la competitività dei sistemi produttivi",
    "teoria e metodi del progetto di architettura, città e paesaggio","strategie e forme delle modificazioni urbane",
    "accessibilità e mobilità: nuovi spazi pubblici e infrastrutture","strategie e sistemi di paesaggio",
    "sperimentazioni progettuali sulla città: aree dismesse e di margine","processi innovativi di trasformazione degli spazi pubblici urbani, attraverso tecniche digitali",
    "exibit e installazioni nella città contemporanea",]
    argomenti['Culture e Società'] = ["Cinema e media","Semiotica","Sociologia del giornalismo",
    "Storia dell'arte","Filosofia sociale","Sociologia dei media digitali","Sociologia dell'amministrazione",
    "Statistica sociale","Marketing","Comunicazione"]
    argomenti['Fisica e Chimica - Emilio Segrè'] = ["Anatomia e istologia apparato oculare",
    "Informatica","Ottica Geometrica","Chimica inorganica","chimica supramolecolare",
    "Sostanze naturali","Fisica statistica","Meccanica quantistica","Spettroscopia","Radiazioni"]
    argomenti['Biomedicina, Neuroscienze e Diagnostica avanzata'] = ["Metodologie proteomiche","Epigenetica",
    "Neurobiologia molecolare","Immunologia","Fisiologia","Patologia","Anatomia","Psichiatria",
    "Riabilitazione Psichiatrica","Medicina legale"]
    argomenti['Scienze e Tecnologie Biologiche Chimiche e Farmaceutiche'] = ["Chimica generale","Chimica inorganica","Biologia animale","Biochimica",
    "Sicurezza nei laboratori","Chimica analitica","Dinamica molecolare",
    "Igiene","Chimica analitica","Scienze dell'alimentazione"]
    argomenti['Promozione della Salute, Materno-Infantile, di Medicina Interna e Specialistica di Eccellenza “G. D’Alessandro”'] =  ["Istologia",
    "Psicologia clinica","Assistenza al parto","Ginecologia","Dermatologia","Scienze biomediche",
    "Produzione degli alimenti","Scienze dietetiche","Infermieristica","Neurologia"]
    argomenti['Discipline Chirurgiche, Oncologiche e Stomatologiche'] = ["Radioterapia",
    "Istologia","Malattie dei tessuti dentali","Paradontologia","Biochimica","Anatomia","Igiene",
    "Farmacologia","Gastroenterologia","Malattie infettive"]


def area_from_dipartimento(name):
    if name == 'Scienze Umanistiche' or name == 'Scienze Psicologiche, Pedagogiche, dell’Esercizio Fisico e della Formazione' or name == 'Scienze Politiche e delle relazioni internazionali' or name == 'Giurisprudenza' or name == 'Promozione della Salute, Materno-Infantile, di Medicina Interna e Specialistica di Eccellenza “G. D’Alessandro”':
        return 11
    elif name == 'Scienze Economiche, Aziendali e Statistiche':
        return 10
    elif name == 'Scienze Agrarie, Alimentari e Forestali':
        return 1
    elif name == 'Scienze della Terra e del Mare':
        return 12
    elif name == 'Matematica e Informatica':
        r = random.randint(0,1)
        if r == 0:
            return 4
        else:
            return 14
    elif name == 'Ingegneria':
        return 7
    elif name == 'Culture e Società':
        return 13
    elif name == 'Architettura':
        return 9
    elif name == 'Fisica e Chimica - Emilio Segrè':
        r = random.randint(0,1)
        if r == 0:
            return 5
        else:
            return 6
    elif name == 'Biomedicina, Neuroscienze e Diagnostica avanzata':
        return 2
    elif name == 'Scienze e Tecnologie Biologiche Chimiche e Farmaceutiche':
        return 6
    elif name == 'Discipline Chirurgiche, Oncologiche e Stomatologiche':
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
    index = random.randint(0,15)
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
