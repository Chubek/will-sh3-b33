from scripts.utilities import download_gdown
from dotenv import dotenv_values
import os
from tensorflow import keras

temp = dotenv_values("env")

def download_deep():
    if not os.path.exists(temp["MODEL_FOLDER"]):
        os.makedirs(temp["MODEL_FOLDER"])

    deep_name = temp["DEEP_NAME"]

    path = os.path.join(temp['MODEL_FOLDER'], deep_name)

    if not os.path.exists(path):
        download_gdown(temp["DEEP_URL"], path)

    return path


def load_deep():
    path = download_deep()

    return keras.models.load_model(path)
