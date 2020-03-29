# https://pypi.org/project/python-codicefiscale/, libreria per generare cf
import os
import numpy as np
import pandas as pd

names = pd.read_csv("../res/datasets/nomi.csv")
surnames = pd.read_csv("../res/datasets/cognomi.csv")

for i in range(0, 100):
    print(names.iloc[np.random.randint(0, 100), 0] + " " +
          surnames.iloc[np.random.randint(0, 100), 0])
