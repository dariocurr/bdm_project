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
