from scripts.utilities import download_gdown
from dotenv import dotenv_values
import os
from transformers import BertForSequenceClassification
from scripts.encode_labels import load_le_status
from config import device
import torch

temp = dotenv_values(".env")

def download_bert():
    if not os.path.exists(temp["MODEL_FOLDER"]):
        os.makedirs(temp["MODEL_FOLDER"])
        
    deep_name = temp["BERT_NAME"]

    path = os.path.join(temp['MODEL_FOLDER'], deep_name)

    if not os.path.exists(path):
        download_gdown(temp["BERT_URL"], path)

    return path


def load_bert():
    path = load_bert()
    
    le_status = load_le_status()
    label_dict = {}

    for cls in le_status.classes_:
        label_dict[cls] = le_status.transform([cls])[0]

    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                      num_labels=len(label_dict),
                                                      output_attentions=False,
                                                      output_hidden_states=False)

    model.to(device)

    return model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))