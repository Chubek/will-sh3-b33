from scripts.load_deep import load_deep
from scripts.encode_labels import load_le_status
import numpy as np

model = load_deep()
le_status = load_le_status()


def classify_deep(input_features):
    pred = model.predict(input_features)

    argmax = np.argmax(pred)

    label = le_status.inverse_transform(argmax)

    return label, argmax[0], pred[argmax[0]]