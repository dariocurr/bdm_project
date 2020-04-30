# GENERAZIONE ATTIVITA' DIDATTICHE
from database_connection import database_connection
import random


# Attivita(id_attivita,nome,descrizione,dipartimento)
def creazioni_attivita():
    attivita_unipa = list()
    attivita_unito = list()
    attivita_unimi = list()
    attivita_unina = list()

    facolta_scientifiche_unito = ["Dipartimento di Economia e Statistica \"Cognetti de Martiis\"",
                                  "Dipartimento di Fisica", "Dipartimento di Informatica", "Dipartimento di Matematica \"Giuseppe Peano\""]
    facolta_scientifiche_unipa = ["Architettura", "Fisica e Chimica - Emilio Segrè",
                                  "Ingegneria", "Matematica e Informatica", "Scienze Economiche, Aziendali e Statistiche"]
    facolta_scientifiche_unimi = ["Dipartimento di Economia, Management e Metodi Quantitativi", "Dipartimento di Fisica Aldo Pontremoli",
                                  "Dipartimento di Informatica Giovanni degli Antoni", "Dipartimento di Matematica Federigo Enriques"]
    facolta_scientifiche_unina = ["Dipartimento di Architettura", "Dipartimento di Economia, Management, Istituzioni", "Dipartimento di Fisica \"Ettore Pancini\"", "Dipartimento di Ingegneria Chimica, dei Materiali e della Produzione Industriale",
                                  "Dipartimento di Ingegneria Civile, Edile e Ambientale", "Dipartimento di Ingegneria Elettrica e delle Tecnologie dell Informazione", "Dipartimento di Ingegneria Industriale", "Dipartimento di Matematica e Applicazioni \"Renato Caccioppoli\"", "Dipartimento di Scienze Economiche e Statistiche", "Dipartimento di Strutture per l Ingegneria e l Architettura"]
    materie_scientifiche = ["Analisi matematica I", "analisi matematica II", "basi di matematica", "Fisica I", "Fisica II", "Logica", "geometria", "algebra lineare", "basi di dati",
                            "basi di informatica", "matematica generale", "termodinamica", "algoritmi", "geometria solida", "calcolo combinatorio", "Attività per l'inserimento nel mondo del lavoro", "programamzione", "calcolo numerico", "lingua inglese B1", "prova finale", "tirocinio", "lingua inglese B2"]

    facolta_mediche_unito = ["Dipartimento di Biotecnologie Molecolari e Scienze per la Salute", "Dipartimento di Neuroscienze \"Rita Levi Montalcini\"", "Dipartimento di Oncologia", "Dipartimento di Scienza e Tecnologia del Farmaco",
                             "Dipartimento di Scienze Chirurgiche", "Dipartimento di Scienze Cliniche e Biologiche", "Dipartimento di Scienze della Sanità Pubblica e Pediatriche", "Dipartimento di Scienze Veterinarie", "Dipartimento di Scienze Mediche"]
    facolta_mediche_unipa = ["Biomedicina, Neuroscienze e Diagnostica avanzata", "Discipline Chirurgiche, Oncologiche e Stomatologiche",
                             "Promozione della Salute, Materno-Infantile, di Medicina Interna e Specialistica di Eccellenza \“G. D’Alessandro\”", "Scienze e Tecnologie Biologiche Chimiche e Farmaceutiche"]
    facolta_mediche_unimi = ["Dipartimento di Medicina Veterinaria", "Dipartimento di Oncologia ed Emato-Oncologia", "Dipartimento di Scienze Biomediche e Cliniche L. Sacco",
                             "Dipartimento di Scienze Biomediche per la Salute", "Dipartimento di Scienze Biomediche, Chirurgiche ed Odontoiatriche", "Dipartimento di Fisiopatologia Medico-Chirurgica e dei Trapianti"]
    facolta_mediche_unina = ["Dipartimento di Farmacia", "Dipartimento di Medicina Clinica e Chirurgia",
                             "Dipartimento di Neuroscienze e Scienze Riproduttive ed Odontostomatologiche", "Dipartimento di Sanità Pubblica"]
    materie_mediche = ["Infermieristica", "Educazione professionale", "fondamenti di matematica", "Fondamenti di fisica", "basi di informatica", "geometria piana", "chimica generale", "chimica biologica", "chimica molecoalre",
                       "biologia generale", "logica e cultura generale", "tirocinio", "prova finale", "Biochimica", "fisica medica", "inglese B1", "genetica", "metodologia medico scientifico", "farmacologia", "lingua inglese B2", "lingua inglese B1"]

    facolta_umanistiche_unito = ["Dipartimento di Culture, Politica e Società", "Dipartimento di Filosofia e Scienze dell’Educazione", "Dipartimento di Giurisprudenza", "Dipartimento di Lingue e Letterature straniere e Culture moderne",
                                 "Dipartimento di Management", "Dipartimento di Psicologia", "Dipartimento di Scienze economico-sociali e matematico-statistiche", "Dipartimento di Studi Storici", "Dipartimento di Studi Umanistici", ]
    facolta_umanistiche_unipa = ["Culture e Società", "Giurisprudenza", "Scienze Politiche e delle relazioni internazionali",
                                 "Scienze Psicologiche, Pedagogiche, dell’Esercizio Fisico e della Formazione", "Scienze Umanistiche"]
    facolta_umanistiche_unimi = ["Dipartimento di Diritto Privato e Storia del Diritto", "Dipartimento di Beni Culturali e Ambientali",
                                 "Dipartimento di Diritto Pubblico Italiano e Sovranazionale", "Dipartimento di Filosofia Piero Martinetti", "Dipartimento di Lingue e Letterature Straniere", ]
    facolta_umanistiche_unina = ["Dipartimento di Giurisprudenza", "Dipartimento di Scienze Politiche",
                                 "Dipartimento di Scienze Sociali", "Dipartimento di Studi Umanistici"]
    materie_umanistiche = ["Storia medievale", "Filosofia", "Letteratura", "Semiotica", "Editoria", "Linguistica", "storia contemporanea", "storia moderna", "antropologia culturale", "filologia romanza", "letteratura italiana",
                           "storia delle tradizioni popolari", "lingua inglese B1", "lingua inglese B2", "filosofia morale", "filosofia teoretica", "storia del diritto", "storia dell'arte medievale", "storia dell'arte moderna", "storia romana", "storia greca"]

    facolta_scientifico_naturali_unito = ["Dipartimento di Chimica", "Dipartimento di Scienze Agrarie, Forestali e Alimentari", "Dipartimento di Scienze della Terra",
                                          "Dipartimento di Scienze della Vita e Biologia dei Sistemi", "Dipartimento Interateneo di Scienze, Progetto e Politiche del Territorio"]
    facolta_scientifico_naturali_unipa = [
        "Scienze Agrarie, Alimentari e Forestali", "Scienze della Terra e del Mare"]
    facolta_scientifico_naturali_unimi = ["Dipartimento di Bioscienze", "Dipartimento di Biotecnologie Mediche e Medicina Traslazionale",
                                          "Dipartimento di Chimica", "Dipartimento di Scienze Agrarie e Ambientali - Produzione, Territorio, Agroenergia"]
    facolta_scientifico_naturali_unina = ["Dipartimento di Agraria", "Dipartimento di Biologia", "Dipartimento di Medicina Molecolare e Biotecnologie Mediche", "Dipartimento di Medicina Veterinaria e Produzioni Animali",
                                          "Dipartimento di Scienze Biomediche Avanzate", "Dipartimento di Scienze Chimiche", "Dipartimento di Scienze della Terra, dell Ambiente e delle Risorse", "Dipartimento di Scienze Mediche Traslazionali"]
    materie_scientifico_naturali = ["fondamenti di chimica", "Fondamenti di amtematica e statistica", "botanica generale", "lingua inglese B1", "lingua inglese B2" "basi di fisica", "chimica organica", "microbiologia",
                                    "biochimica", "biologia molecolare", "fisiologia vegetale", "biologia dello sviluppo", "ecologia generale ed applicata", "fisiologia generale", "citologia e istologia", "zoologia generale e sistematica"]

# ATTIVITA' PER I DIPARTIMENTI SCIENTIFICI
# UNIPA

    for facolta in facolta_scientifiche_unipa:
        tmp = materie_scientifiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unipa.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])

# UNITO
    for facolta in facolta_scientifiche_unito:
        tmp = materie_scientifiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unito.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])

# UNIMI
    for facolta in facolta_scientifiche_unimi:
        tmp = materie_scientifiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unimi.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# UNINA
    for facolta in facolta_scientifiche_unina:
        tmp = materie_scientifiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unina.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])

# ATTIVITA' PER I DIPARTIMENTI MEDICI
# UNIPA

    for facolta in facolta_mediche_unipa:
        tmp = materie_mediche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unipa.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])

# UNITO
    for facolta in facolta_mediche_unito:
        tmp = materie_mediche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unito.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# UNIMI
    for facolta in facolta_mediche_unimi:
        tmp = materie_mediche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unimi.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# UNINA
    for facolta in facolta_mediche_unina:
        tmp = materie_mediche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unina.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# ATTIVITA' PER I DIPARTIMENTI UMANISTICI
# UNIPA

    for facolta in facolta_umanistiche_unipa:
        tmp = materie_umanistiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unipa.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])

# UNITO
    for facolta in facolta_umanistiche_unito:
        tmp = materie_umanistiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unito.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# UNIMI
    for facolta in facolta_umanistiche_unimi:
        tmp = materie_umanistiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unimi.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# UNINA
    for facolta in facolta_umanistiche_unina:
        tmp = materie_umanistiche.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unina.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])

# ATTIVITA' PER I DIPARTIMENTI SCIENTIFICO NATURALI
# UNIPA

    for facolta in facolta_scientifico_naturali_unipa:
        tmp = materie_scientifico_naturali.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unipa.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])

# UNITO
    for facolta in facolta_scientifico_naturali_unito:
        tmp = materie_scientifico_naturali.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unito.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# UNIMI
    for facolta in facolta_scientifico_naturali_unimi:
        tmp = materie_scientifico_naturali.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unimi.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])


# UNINA
    for facolta in facolta_scientifico_naturali_unina:
        tmp = materie_scientifico_naturali.copy()
        for i in range(0, 10):
            x = random.randint(0, len(tmp) - 1)
            attivita_unina.append([tmp[x], "", facolta])
            tmp.remove(tmp[x])
    print("UNIPA\n")
    print(attivita_unipa)
    print("UNITO\n")
    print(attivita_unito)
    print("UNIMI\n")
    print(attivita_unimi)
    print("UNINA\n")
    print(attivita_unina)


creazioni_attivita()
