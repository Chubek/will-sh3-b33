from scripts.load_bert import load_bert
from scripts.load_tokenizer import load_tokenizer
from scripts.encode_labels import load_le_status
from config import device
import numpy as np

model = load_bert()
tokenizer = load_tokenizer()
le_status = load_le_status()

def classify_essay(essay_text):
    inputs = tokenizer(essay_text, return_tensors="pt", max_length=512, truncation=True)

    inputs.to(device)

    outputs = model(**inputs)

    argmax = np.argmax(outputs)

    label = le_status.inverse_transform(argmax)[0]

    return label, int(argmax[0]), float(outputs[argmax[0]])