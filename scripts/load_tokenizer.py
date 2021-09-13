import json
from dotenv import dotenv_values
import os
from scripts.utilities import download_gdown
from transformers import BertTokenizer

temp = dotenv_values(".env")


def download_all_tokenizer():
    tok_folder = os.path.join(temp["MODEL_FOLDER"], temp["TOK_FOLDER"])
    if not os.path.exists(tok_folder):
        os.makedirs(tok_folder)


    dict_urls = json.loads(temp['TOK_JSON'])

    for k, v in dict_urls:
        path = os.path.join(tok_folder, k)
        if not os.path.exists(path):
            download_gdown(v, path)

    return tok_folder


def load_tokenizer():
    path = download_all_tokenizer()

    return BertTokenizer.from_pretrained(path)






