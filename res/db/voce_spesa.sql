CREATE TABLE universita (
    id_universita INT PRIMARY KEY AUTO_INCREMENT,
    nome TEXT NOT NULL,
    citta VARCHAR(30)
);

CREATE TABLE dipartimento (
  id_dipartimento INT PRIMARY KEY AUTO_INCREMENT,
  nome TEXT NOT NULL,
  id_dipartimento INT,
  FOREIGN KEY(id_dipartimento) REFERENCES universita(id_universita)
);

CREATE TABLE fondo (
  id_fondo INT PRIMARY KEY AUTO_INCREMENT,
  budget DECIMAL(15, 2),
  data DATE,
  nome_ente TEXT,
  dipartimento INT,
  FOREIGN KEY(dipartimento) REFERENCES dipartimento(id_dipartimento)
);

CREATE TABLE voce_fondo (
    id_voce_fondo INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    descrizione TEXT,
    importo DECIMAL(15, 2) NOT NULL,
    fondo INT,
    FOREIGN KEY(fondo) REFERENCES fondo(id_fondo)
);

CREATE TABLE area_ricerca (
    id_area_ricerca INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    descrizione TEXT
);

CREATE TABLE progetto (
  id_progetto INT PRIMARY KEY AUTO_INCREMENT,
  nome TEXT NOT NULL,
  descrizione TEXT,
  data_avvio DATE,
  data_fine DATE,
  budget DECIMAL(15, 2),
  id_area_ricerca INT,
  FOREIGN KEY(id_area_ricerca) REFERENCES area_ricerca(id_area_ricerca)
);

CREATE TABLE personale_non_strutturato (
  id_personale_non_strutturato INT PRIMARY KEY AUTO_INCREMENT,
  tipologia_contratto TEXT
);

CREATE TABLE data (
    id_data DATE PRIMARY KEY,
    anno YEAR,
    mese INT(2)
);

CREATE TABLE voce_spesa (
  id_voce_spesa INT PRIMARY KEY AUTO_INCREMENT,
  id_voce_fondo INT,
  id_personale_non_strutturato INT,
  id_progetto INT,
  id_data DATE,
  importo DECIMAL(15, 2),
  FOREIGN KEY(id_voce_fondo) REFERENCES fondo(id_fondo),
  FOREIGN KEY(id_personale_non_strutturato) REFERENCES personale_non_strutturato(id_personale_non_strutturato),
  FOREIGN KEY(id_progetto) REFERENCES progetto(id_progetto),
  FOREIGN KEY(id_data) REFERENCES data(id_data)
);
