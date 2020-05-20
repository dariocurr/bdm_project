CREATE TABLE universita (
    id_universita INT PRIMARY KEY,
    nome TEXT NOT NULL,
    citta VARCHAR(30)
);

CREATE TABLE dipartimento (
    id_dipartimento INT PRIMARY KEY,
    nome TEXT NOT NULL,
    universita INT,
    FOREIGN KEY(universita) REFERENCES universita(id_universita)
);

CREATE TABLE tipologia (
    tipologia VARCHAR(100) PRIMARY KEY
);

CREATE TABLE argomento (
    argomento VARCHAR(100) PRIMARY KEY
);

CREATE TABLE data (
    data DATE PRIMARY KEY,
    anno YEAR,
    mese INT(2)
);

CREATE TABLE evento (
    data DATE,
    tipologia VARCHAR(100),
    dipartimento INT,
    argomento VARCHAR(100),
    portata INT,
    partitecipanti_previsti INT,
    partitecipanti_effettivi INT,
    ricavo DECIMAL(15, 2),
    FOREIGN KEY(data) REFERENCES data(data),
    FOREIGN KEY(tipologia) REFERENCES tipologia(tipologia),
    FOREIGN KEY(argomento) REFERENCES argomento(argomento),
    FOREIGN KEY(dipartimento) REFERENCES dipartimento(id_dipartimento),
    PRIMARY KEY(tipologia, dipartimento, argomento, data)
);
