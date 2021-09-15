from scripts.utilities import download_gdown
from dotenv import dotenv_values
import os
import joblib

temp = dotenv_values("env")


def download_grad_boost():
    if not os.path.exists(temp["MODEL_FOLDER"]):
        os.makedirs(temp["MODEL_FOLDER"])

    grad_boost_name = temp["GRAD_BOOST_NAME"]

    path = os.path.join(temp['MODEL_FOLDER'], grad_boost_name)

    if not os.path.exists(path):
        download_gdown(temp["GRAD_BOOST_URL"], path)

    return path


def download_svm():
    if not os.path.exists(temp["MODEL_FOLDER"]):
        os.makedirs(temp["MODEL_FOLDER"])

    svm_name = temp["SVM_NAME"]

    path = os.path.join(temp['MODEL_FOLDER'], svm_name)

    if not os.path.exists(path):
        download_gdown(temp["SVM_URL"], path)

    return path

def load_grad_boost():
    path = download_grad_boost()

    return joblib.load(path)


def load_svm():
    path = download_svm()

    return joblib.load(path)