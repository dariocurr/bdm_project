# https://pypi.org/project/python-codicefiscale/, libreria per generare cf
import datetime
import random
import numpy as np
import pandas as pd
from codicefiscale import codicefiscale


names = pd.read_csv("../res/datasets/nomi.csv")
surnames = pd.read_csv("../res/datasets/cognomi.csv")
hospitals = pd.read_csv("../res/datasets/ospedali.csv")

for i in range(0, 100):
    name = names.iloc[np.random.randint(0, 100), 0]
    surname = surnames.iloc[np.random.randint(0, 100), 0]
    day = np.random.randint(1, 32)
    month = np.random.randint(1, 13)
    year = np.random.randint(1950, 1995)
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(2000, 12, 31)
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
    print(codice_fiscale)
