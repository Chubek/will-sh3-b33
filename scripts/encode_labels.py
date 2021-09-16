from dotenv import dotenv_values
import os
import inspect
import joblib
from scripts.utilities import download_gdown
from copy import deepcopy

temp = dotenv_values("env")

def retrieve_name(var):
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]




def download_all_les():
    if not os.path.exists(temp["MODEL_FOLDER"]):
        os.makedirs(temp["MODEL_FOLDER"])

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


def load_all_les():
    download_all_les()    

    le_status = "le_status"
    le_sex = "le_sex"
    le_orientation = "le_orientation" 
    le_body_type = "le_body_type"
    le_diet = "le_diet"
    le_drinks = "le_drinks"
    le_drugs = "le_drugs"
    le_ethnicity = "le_ethnicity"
    le_offspring = "le_offspring"
    le_pets = "le_pets"
    le_sign = "le_sign"
    le_smokes = "le_smokes"
    sc_age = "sc_age"
    sc_height = "sc_height"
    sc_income = "sc_income"

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

    dict_all = {}

    for le in list_all:
        name_copy = deepcopy(le)
        name = le + ".pkl"
        path = os.path.join(temp['MODEL_FOLDER'], name)

        le = joblib.load(path)

        dict_all[name_copy] = le


    return dict_all


def get_classes(le):
    return le.classes_

def encode_class(le, cls):
    return le.transform([cls])

def decode_label(le, lab):
    return le.inverse_transform([lab])


def get_json_lab_cls(le_dict):
    fin_json = {}

    for k, v in le_dict.items():
        if not "sc" in k:
            k_name = "_".join(k.split("_")[1:]).capitalize()
            fin_json[k_name] = [{"text": l, "value": m} for l, m in zip(get_classes(v).tolist(), [int(encode_class(v, n)[0]) for n in get_classes(v).tolist()])]


    return fin_json



def load_le_status():
    le_status = temp['LE_STATUS']

    name = "le_status.pkl"
    path = os.path.join(temp['MODEL_FOLDER'], name)

    if not os.path.exists(path):
        download_gdown(le_status, path)

    le_status = joblib.load(path)

    return le_status