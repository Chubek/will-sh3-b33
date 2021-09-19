import pandas as pd
import os
import random

df = pd.read_csv(os.path.join(os.getcwd(), 'scripts', "data", "df_nlp_50.csv"))

def serve_random():
    rand_num = random.randint(0, len(df))

    return df.loc[rand_num, "all_full"]