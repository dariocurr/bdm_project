CREATE TABLE ente (
  id_ente INT PRIMARY KEY AUTO_INCREMENT,
  nome TEXT NOT NULL,
  descrizione TEXT,
  livello TEXT,
  indirizzo TEXT
);

CREATE TABLE fondo (
  id_fondo INT PRIMARY KEY AUTO_INCREMENT,
  nome TEXT NOT NULL,
  budget DECIMAL(15, 2),
  data DATE,
  ente INT,
  FOREIGN KEY(ente) REFERENCES ente(id_ente)
);

CREATE TABLE dipartimento (
  id_dipartimento INT PRIMARY KEY AUTO_INCREMENT,
  nome TEXT NOT NULL,
  indirizzo TEXT,
  fondo INT,
  FOREIGN KEY(fondo) REFERENCES fondo(id_fondo)
);

CREATE TABLE archivio_dipartimentale (
  id_archivio_dipartimentale INT PRIMARY KEY AUTO_INCREMENT,
  dipartimento INT,
  FOREIGN KEY(dipartimento) REFERENCES dipartimento(id_dipartimento)
);

CREATE TABLE personale (
    cf CHAR(16) PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    cognome VARCHAR(30) NOT NULL,
    data_nascita DATE,
    residenza TEXT,
    dipartimento INT,
    FOREIGN KEY(dipartimento) REFERENCES dipartimento(id_dipartimento)
);

CREATE TABLE personale_ta (
    id_pta INT PRIMARY KEY AUTO_INCREMENT,
    livello TEXT,
    stipendio DECIMAL(15, 2),
    qualifica TEXT,
    telefono VARCHAR(15),
    anagrafica_personale CHAR(16),
    FOREIGN KEY(anagrafica_personale) REFERENCES personale(cf)
);

CREATE TABLE personale_ricerca (
  id_personale_ricerca INT PRIMARY KEY AUTO_INCREMENT,
  tipologia_contratto TEXT,
  stipendio DECIMAL(15, 2),
  anagrafica_personale CHAR(16),
  FOREIGN KEY(anagrafica_personale) REFERENCES personale(cf)
);

CREATE TABLE personale_strutturato (
    id_personale_strutturato INT PRIMARY KEY AUTO_INCREMENT,
    telefono VARCHAR(15),
    ufficio TEXT,
    personale_ricerca INT,
    FOREIGN KEY(personale_ricerca) REFERENCES personale_ricerca(id_personale_ricerca)
);

CREATE TABLE personale_non_strutturato (
  id_personale_non_strutturato INT PRIMARY KEY AUTO_INCREMENT,
  laboratorio_riferimento TEXT,
  telefono VARCHAR(15),
  personale_ricerca INT,
  FOREIGN KEY(personale_ricerca) REFERENCES personale_ricerca(id_personale_ricerca)
);

CREATE TABLE area_ricerca (
    id_area_ricerca INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    descrizione TEXT
);

CREATE TABLE pubblicazione (
  id_pubblicazione INT PRIMARY KEY AUTO_INCREMENT,
  titolo TEXT NOT NULL,
  data_pubblicazione DATE,
  nome_rivista TEXT,
  tipologia TEXT,
  id_area_ricerca INT,
  indice_qualita INT,
  FOREIGN KEY(id_area_ricerca) REFERENCES area_ricerca(id_area_ricerca)
);

CREATE TABLE progetto_ricerca (
  id_progetto INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(30) NOT NULL,
  descrizione TEXT,
  data_avvio DATE,
  data_fine DATE,
  budget DECIMAL(15, 2),
  id_area_ricerca INT,
  FOREIGN KEY(id_area_ricerca) REFERENCES area_ricerca(id_area_ricerca)
);

CREATE TABLE evento (
    id_evento INT PRIMARY KEY AUTO_INCREMENT,
    titolo TEXT NOT NULL,
    tipo TEXT,
    data DATE,
    durata TIME,
    portata INT,
    luogo_evento TEXT,
    partitecipanti_previsti INT,
    partitecipanti_effettivi INT,
    ricavo DECIMAL(15, 2),
    progetto_ricerca INT,
    archivio_dipartimentale INT,
    FOREIGN KEY(progetto_ricerca) REFERENCES progetto_ricerca(id_progetto),
    FOREIGN KEY(archivio_dipartimentale) REFERENCES archivio_dipartimentale(id_archivio_dipartimentale)
);

CREATE TABLE attivita_didattica (
  id_attivita_didattica INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  descrizione TEXT,
  facoltà TEXT
);

CREATE TABLE agenzia_esterna (
  id_agenzia INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  descrizione TEXT,
  tipologia TEXT,
  indirizzo TEXT
);

CREATE TABLE voce_fondo (
    id_voce_fondo INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    descrizione TEXT,
    importo DECIMAL(15, 2) NOT NULL,
    data DATE,
    fondo INT,
    FOREIGN KEY(fondo) REFERENCES fondo(id_fondo)
);

CREATE TABLE voce_spesa (
  id_voce_spesa INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  descrizione TEXT,
  importo DECIMAL(15, 2),
  copertura INT,
  FOREIGN KEY(copertura) REFERENCES fondo(id_fondo)
);

CREATE TABLE organizza (
  personale_strutturato INT,
  evento INT,
  FOREIGN KEY(personale_strutturato) REFERENCES personale_strutturato(id_personale_strutturato),
  FOREIGN KEY(evento) REFERENCES evento(id_evento)
);

CREATE TABLE collabora_1 (
  personale CHAR(16),
  evento INT,
  FOREIGN KEY(personale) REFERENCES personale(cf),
  FOREIGN KEY(evento) REFERENCES evento(id_evento)
);

CREATE TABLE collabora_2 (
    evento INT,
    agenzia_esterna INT,
    data_intervento DATE,
    descrizione_intervento TEXT,
    FOREIGN KEY(evento) REFERENCES evento(id_evento),
    FOREIGN KEY(agenzia_esterna) REFERENCES agenzia_esterna(id_agenzia)
);

CREATE TABLE retribuisce (
  voce_spesa INT,
  personale_non_strutturato INT,
  FOREIGN KEY(voce_spesa) REFERENCES voce_spesa(id_voce_spesa),
  FOREIGN KEY(personale_non_strutturato) REFERENCES personale_non_strutturato(id_personale_non_strutturato)
);

CREATE TABLE finanzia_3 (
  voce_spesa INT,
  progetto_ricerca INT,
  FOREIGN KEY(voce_spesa) REFERENCES voce_spesa(id_voce_spesa),
  FOREIGN KEY(progetto_ricerca) REFERENCES progetto_ricerca(id_progetto)
);

CREATE TABLE finanzia_2 (
  voce_spesa INT,
  evento INT,
  FOREIGN KEY(voce_spesa) REFERENCES voce_spesa(id_voce_spesa),
  FOREIGN KEY(evento) REFERENCES evento(id_evento)
);

CREATE TABLE dirige (
  personale_strutturato INT,
  progetto_ricerca INT,
  da_data DATE,
  FOREIGN KEY(progetto_ricerca) REFERENCES progetto_ricerca(id_progetto),
  FOREIGN KEY(personale_strutturato) REFERENCES personale_strutturato(id_personale_strutturato)
);

CREATE TABLE mantiene (
  progetto_ricerca INT,
  attivita_didattica INT,
  ruolo VARCHAR(30),
  anno_accademico VARCHAR(9),
  FOREIGN KEY(progetto_ricerca) REFERENCES progetto_ricerca(id_progetto),
  FOREIGN KEY(attivita_didattica) REFERENCES attivita_didattica(id_attivita_didattica)
);

CREATE TABLE pubblica (
  pubblicazione INT,
  personale_ricerca INT,
  ordine TEXT,
  FOREIGN KEY(pubblicazione) REFERENCES pubblicazione(id_pubblicazione),
  FOREIGN KEY(personale_ricerca) REFERENCES personale_ricerca(id_personale_ricerca)
);

CREATE TABLE partecipa_2 (
  personale_ricerca INT,
  progetto_ricerca INT,
  ruolo VARCHAR(30),
  FOREIGN KEY(personale_ricerca) REFERENCES personale_ricerca(id_personale_ricerca),
  FOREIGN KEY(progetto_ricerca) REFERENCES progetto_ricerca(id_progetto)
);

CREATE TABLE ruolo (
  id_ruolo INT PRIMARY KEY AUTO_INCREMENT,
  data_inizio DATE,
  data_fine DATE,
  stipendio DECIMAL(15, 2),
  tipologia_contratto TEXT,
  personale_ricerca INT,
  FOREIGN KEY(personale_ricerca) REFERENCES personale_ricerca(id_personale_ricerca)
);

CREATE TABLE contiene_1 (
  archivio_dipartimentale INT,
  pubblicazione INT,
  FOREIGN KEY(archivio_dipartimentale) REFERENCES archivio_dipartimentale(id_archivio_dipartimentale),
  FOREIGN KEY(pubblicazione) REFERENCES pubblicazione(id_pubblicazione)
);

CREATE TABLE contiene_3 (
  archivio_dipartimentale INT,
  progetto_ricerca INT,
  FOREIGN KEY(archivio_dipartimentale) REFERENCES archivio_dipartimentale(id_archivio_dipartimentale),
  FOREIGN KEY(progetto_ricerca) REFERENCES progetto_ricerca(id_progetto)
);
