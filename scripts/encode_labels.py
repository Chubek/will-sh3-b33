import gdown
from dotenv import dotenv_values
import os
import inspect

temp = dotenv_values(".env")

def retrieve_name(var):
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]

def download_gdown(url, path):
    gdown.download(url, path, quiet=False)


def dowload_all_models():
    le_status = temp['LE_STATUS']
    le_sex = temp['LE_SEX']
    le_orientation = temp['LE_ORIENTATION']
    le_body_type = temp['LE_BODY_TYPE']
    le_diet = temp['LE_DIET']
    le_drinks = temp['LE_DRINKS']
    le_drugs = temp['LE_DRUGS']
    le_ethnicity = temp['LE_ETHNICITY']
    le_offspring = temp['LE_OFFSPRING']
    le_pets = temp['LE_PETS']
    le_sign = temp['LE_SIGN']
    le_smokes = temp['LE_SMOKES']
    sc_age = temp['SC_AGE']
    sc_height = temp['SC_HEIGHT']
    sc_income = temp['SC_INCOME']

    list_all = [le_status,
            le_sex,
            le_orientation, 
            le_body_type, 
            le_diet, 
            le_drinks,
            le_drugs,
            le_ethnicity,
            le_offspring,
            le_pets,
            le_sign,
            le_smokes,
            sc_age,
            sc_height,
            sc_income]


    for le in list_all:
        name = retrieve_name(le) + ".pkl"
        path = os.path.join(temp['MODEL_FOLDER'], name)

        if not os.path.exists(path):
            download_gdown(le, path)