from scripts.classify_deep import classify_deep
from scripts.classify_essay import classify_essay
from scripts.classify_shallow import classify_gb, classify_svm
from scripts.encode_labels import load_all_les
from flask import Flask, request, jsonify, send_from_directory


app = Flask(__name__, static_url_path='/static')

le_dict = load_all_les()

@app.route("/")
def root():
    return app.send_static_file("index.html")


@app.route("/classify_essay", methods=["POST"])
def classify_text():
    essay = request.form["essay"]

    cls, label, prob  = classify_essay(essay)

    return jsonify({"class": cls, "label": label, "prob": prob})


@app.route("/classify_deep", methods=["POST"])
def classify_deep():
    sex = le_dict["le_sex"].transform([int(request.form["sex"])])
    orientation = le_dict["le_orientation"].transform([int(request.form["orientation"])])
    body_type = le_dict["le_body_type"].transform([int(request.form["body_type"])])
    diet = le_dict["le_diet"].transform([int(request.form["diet"])])
    drinks = le_dict["le_drinks"].transform([int(request.form["drinks"])])
    drugs = le_dict["le_drugs"].transform([int(request.form["drugs"])])
    ethnicity = le_dict["le_ethnicity"].transform([int(request.form["ethnicity"])])
    offspring = le_dict["le_offspring"].transform([int(request.form["offspring"])])
    pets = le_dict["le_pets"].transform([int(request.form["pets"])])
    sign = le_dict["le_sign"].transform([int(request.form["sign"])])
    smokes = le_dict["le_smokes"].transform([int(request.form["smokes"])])
    age = le_dict["sc_age"].transform([int(request.form["age"])])
    height = le_dict["sc_height"].transform([int(request.form["height"])])
    income = le_dict["sc_income"].transform([int(request.form["income"])])

    input_features = [
        sex,
        orientation,
        body_type,
        diet,
        drinks,
        drugs,
        ethnicity,
        offspring,
        pets,
        sign,
        smokes,
        age,
        height,
        income
    ]



    cls, label, prob  = classify_deep(input_features)

    return jsonify({"class": cls, "label": label, "prob": prob})

@app.route("/classify_svm", methods=["POST"])
def classify_svm():
    sex = le_dict["le_sex"].transform([int(request.form["sex"])])
    orientation = le_dict["le_orientation"].transform([int(request.form["orientation"])])
    body_type = le_dict["le_body_type"].transform([int(request.form["body_type"])])
    diet = le_dict["le_diet"].transform([int(request.form["diet"])])
    drinks = le_dict["le_drinks"].transform([int(request.form["drinks"])])
    drugs = le_dict["le_drugs"].transform([int(request.form["drugs"])])
    ethnicity = le_dict["le_ethnicity"].transform([int(request.form["ethnicity"])])
    offspring = le_dict["le_offspring"].transform([int(request.form["offspring"])])
    pets = le_dict["le_pets"].transform([int(request.form["pets"])])
    sign = le_dict["le_sign"].transform([int(request.form["sign"])])
    smokes = le_dict["le_smokes"].transform([int(request.form["smokes"])])
    age = le_dict["sc_age"].transform([int(request.form["age"])])
    height = le_dict["sc_height"].transform([int(request.form["height"])])
    income = le_dict["sc_income"].transform([int(request.form["income"])])

    input_features = [
        sex,
        orientation,
        body_type,
        diet,
        drinks,
        drugs,
        ethnicity,
        offspring,
        pets,
        sign,
        smokes,
        age,
        height,
        income
    ]



    cls, label  = classify_svm(input_features)

    return jsonify({"class": cls, "label": label})



@app.route("/classify_gb", methods=["POST"])
def classify_gb():
    sex = le_dict["le_sex"].transform([int(request.form["sex"])])
    orientation = le_dict["le_orientation"].transform([int(request.form["orientation"])])
    body_type = le_dict["le_body_type"].transform([int(request.form["body_type"])])
    diet = le_dict["le_diet"].transform([int(request.form["diet"])])
    drinks = le_dict["le_drinks"].transform([int(request.form["drinks"])])
    drugs = le_dict["le_drugs"].transform([int(request.form["drugs"])])
    ethnicity = le_dict["le_ethnicity"].transform([int(request.form["ethnicity"])])
    offspring = le_dict["le_offspring"].transform([int(request.form["offspring"])])
    pets = le_dict["le_pets"].transform([int(request.form["pets"])])
    sign = le_dict["le_sign"].transform([int(request.form["sign"])])
    smokes = le_dict["le_smokes"].transform([int(request.form["smokes"])])
    age = le_dict["sc_age"].transform([int(request.form["age"])])
    height = le_dict["sc_height"].transform([int(request.form["height"])])
    income = le_dict["sc_income"].transform([int(request.form["income"])])

    input_features = [
        sex,
        orientation,
        body_type,
        diet,
        drinks,
        drugs,
        ethnicity,
        offspring,
        pets,
        sign,
        smokes,
        age,
        height,
        income
    ]



    cls, label  = classify_gb(input_features)

    return jsonify({"class": cls, "label": label})