from scripts.encode_labels import load_le_status
from scripts.load_shallow import load_grad_boost, load_svm


le_status = load_le_status()
model_gb = load_grad_boost()
model_svm = load_svm()


def classify_svm(input_features):
    pred = model_svm.predict([input_features])

    return le_status.inverse_transform(pred), pred[0]

def classify_gb(input_features):
    pred = model_gb.predict([input_features])

    return le_status.inverse_transform(pred), pred[0]
