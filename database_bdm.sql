CREATE TABLE personale (
    cf CHAR(5) PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    cognome VARCHAR(20) NOT NULL,
    data_nascita DATE NOT NULL,
    residenza VARCHAR(20)
);

CREATE TABLE personale_ta (
    id_pta INT PRIMARY KEY AUTO_INCREMENT,
    livello VARCHAR(20),
    stipendio DECIMAL(15, 2) NOT NULL,
    qualifica VARCHAR(20),
    telefono VARCHAR(15),
    anagrafica_personale CHAR(16),
    FOREIGN KEY(anagrafica_personale) REFERENCES personale(cf)
);

CREATE TABLE personale_ricerca (
  id_personale_ricerca INT PRIMARY KEY AUTO_INCREMENT,
  tipologia_contratto VARCHAR(50),
  stipendio DECIMAL(15, 2) NOT NULL,
  anagrafica_personale CHAR(16),
  FOREIGN KEY(anagrafica_personale) REFERENCES personale(cf)
)


CREATE TABLE personale_non_strutturato (
  id_personale_nonstrutturato INT PRIMARY KEY AUTO_INCREMENT
  laboratorio_riferimento VARCHAR(20)
  telefono VARCHAR(15)
  FOREIGN KEY(personale_ricerca) REFERENCES
)


CREATE TABLE evento (
    id_evento INT PRIMARY KEY AUTO_INCREMENT,
    titolo VARCHAR(20) NOT NULL,
    tipo VARCHAR(20),
    data DATE NOT NULL,

)

CREATE TABLE pubblicazione (

)


CREATE TABLE retribuisce (

)
