    """
    #GENERAZIONE PERSONALE
        else:
            #PERSONALE STRUTTURATO
            if random_number == 2:
                promozioni = list()
                if random_number < 2:
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
                    prima_promozione_anno_inizio = np.random.randint(1990, 2010)
                    prima_promozione_anno_fine = np.random.randint(prima_promozione_anno_inizio, 2015)
                    vecchio_stipendio = (prima_promozione_anno_fine - int(date[:4])) * 6.34 + 1478.11
                    promozioni.append((str(prima_promozione_anno_inizio) + "/01/01", str(prima_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
                    seconda_promozione_anno_inizio = np.random.randint(prima_promozione_anno_fine, 2018)
                    seconda_promozione_anno_fine = np.random.randint(seconda_promozione_anno_inizio, 2019)
                    vecchio_stipendio = (seconda_promozione_anno_fine - int(date[:4])) * 6.34 + 1802.89
                    promozioni.append((str(seconda_promozione_anno_inizio) + "/01/01", str(seconda_promozione_anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[2]))
                elif random_number < 6:
                    anno_inizio = np.random.randint(2000, 2018)
                    anno_fine = np.random.randint(anno_inizio, 2019)
                    vecchio_stipendio = (anno_fine - int(date[:4])) * 6.34 + 1478.11
                    promozioni.append((str(anno_inizio) + "/01/01", str(anno_fine) + "/31/12", vecchio_stipendio, tipologia_contratto_strutturato[3]))
                else:
    """
