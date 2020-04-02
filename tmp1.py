import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

confirmed_file = './csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df = pd.read_csv(confirmed_file)
print(df.info())
