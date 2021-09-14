from scripts.classify_deep import classify_deep
from scripts.classify_essay import classify_essay
from scripts.classify_shallow import classify_gb, classify_svm
from scripts.encode_labels import load_all_les, get_json_lab_cls
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

@app.route("/get_all_les")
def get_all_les():
    return jsonify(get_json_lab_cls(le_dict))


@app.route("/classify_deep", methods=["POST"])
def classify_deep_func():
    if request.form["mode"] == "text_label":
        sex = int(le_dict["le_sex"].transform([[request.form["sex"]]])[0])
        orientation = int(le_dict["le_orientation"].transform([[request.form["orientation"]]])[0])
        body_type = int(le_dict["le_body_type"].transform([[request.form["body_type"]]])[0])
        diet = int(le_dict["le_diet"].transform([[request.form["diet"]]])[0])
        drinks = int(le_dict["le_drinks"].transform([[request.form["drinks"]]])[0])
        drugs = int(le_dict["le_drugs"].transform([[request.form["drugs"]]])[0])
        ethnicity = int(le_dict["le_ethnicity"].transform([[request.form["ethnicity"]]])[0])
        offspring = int(le_dict["le_offspring"].transform([[request.form["offspring"]]])[0])
        pets = int(le_dict["le_pets"].transform([[request.form["pets"]]])[0])
        sign = int(le_dict["le_sign"].transform([[request.form["sign"]]])[0])
        smokes = int(le_dict["le_smokes"].transform([[request.form["smokes"]]])[0])
        age = int(le_dict["sc_age"].transform([[request.form["age"]]])[0])
        height = int(le_dict["sc_height"].transform([[request.form["height"]]])[0])
        income = int(le_dict["sc_income"].transform([[request.form["income"]]])[0])
    elif request.form["mode"] == "int_label":    
        sex = int(request.form["sex"])
        orientation = int(request.form["orientation"])
        body_type = int(request.form["body_type"])
        diet = int(request.form["diet"])
        drinks = int(request.form["drinks"])
        drugs = int(request.form["drugs"])
        ethnicity = int(request.form["ethnicity"])
        offspring = int(request.form["offspring"])
        pets = int(request.form["pets"])
        sign = int(request.form["sign"])
        smokes = int(request.form["smokes"])
        age = int(le_dict["sc_age"].transform([[request.form["age"]]])[0])
        height = int(le_dict["sc_height"].transform([[request.form["height"]]])[0])
        income = int(le_dict["sc_income"].transform([[request.form["income"]]])[0])

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
def classify_svm_func():
    if request.form["mode"] == "text_label":
        sex = int(le_dict["le_sex"].transform([[request.form["sex"]]])[0])
        orientation = int(le_dict["le_orientation"].transform([[request.form["orientation"]]])[0])
        body_type = int(le_dict["le_body_type"].transform([[request.form["body_type"]]])[0])
        diet = int(le_dict["le_diet"].transform([[request.form["diet"]]])[0])
        drinks = int(le_dict["le_drinks"].transform([[request.form["drinks"]]])[0])
        drugs = int(le_dict["le_drugs"].transform([[request.form["drugs"]]])[0])
        ethnicity = int(le_dict["le_ethnicity"].transform([[request.form["ethnicity"]]])[0])
        offspring = int(le_dict["le_offspring"].transform([[request.form["offspring"]]])[0])
        pets = int(le_dict["le_pets"].transform([[request.form["pets"]]])[0])
        sign = int(le_dict["le_sign"].transform([[request.form["sign"]]])[0])
        smokes = int(le_dict["le_smokes"].transform([[request.form["smokes"]]])[0])
        age = int(le_dict["sc_age"].transform([[request.form["age"]]])[0])
        height = int(le_dict["sc_height"].transform([[request.form["height"]]])[0])
        income = int(le_dict["sc_income"].transform([[request.form["income"]]])[0])    
    elif request.form["mode"] == "int_label":    
        sex = int(request.form["sex"])
        orientation = int(request.form["orientation"])
        body_type = int(request.form["body_type"])
        diet = int(request.form["diet"])
        drinks = int(request.form["drinks"])
        drugs = int(request.form["drugs"])
        ethnicity = int(request.form["ethnicity"])
        offspring = int(request.form["offspring"])
        pets = int(request.form["pets"])
        sign = int(request.form["sign"])
        smokes = int(request.form["smokes"])
        age = int(le_dict["sc_age"].transform([[request.form["age"]]])[0])
        height = int(le_dict["sc_height"].transform([[request.form["height"]]])[0])
        income = int(le_dict["sc_income"].transform([[request.form["income"]]])[0])
    
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
def classify_gb_func():
    if request.form["mode"] == "text_label":
        sex = int(le_dict["le_sex"].transform([[request.form["sex"]]])[0])
        orientation = int(le_dict["le_orientation"].transform([[request.form["orientation"]]])[0])
        body_type = int(le_dict["le_body_type"].transform([[request.form["body_type"]]])[0])
        diet = int(le_dict["le_diet"].transform([[request.form["diet"]]])[0])
        drinks = int(le_dict["le_drinks"].transform([[request.form["drinks"]]])[0])
        drugs = int(le_dict["le_drugs"].transform([[request.form["drugs"]]])[0])
        ethnicity = int(le_dict["le_ethnicity"].transform([[request.form["ethnicity"]]])[0])
        offspring = int(le_dict["le_offspring"].transform([[request.form["offspring"]]])[0])
        pets = int(le_dict["le_pets"].transform([[request.form["pets"]]])[0])
        sign = int(le_dict["le_sign"].transform([[request.form["sign"]]])[0])
        smokes = int(le_dict["le_smokes"].transform([[request.form["smokes"]]])[0])
        age = int(le_dict["sc_age"].transform([[request.form["age"]]])[0])
        height = int(le_dict["sc_height"].transform([[request.form["height"]]])[0])
        income = int(le_dict["sc_income"].transform([[request.form["income"]]])[0])
    elif request.form["mode"] == "int_label":    
        sex = int(request.form["sex"])
        orientation = int(request.form["orientation"])
        body_type = int(request.form["body_type"])
        diet = int(request.form["diet"])
        drinks = int(request.form["drinks"])
        drugs = int(request.form["drugs"])
        ethnicity = int(request.form["ethnicity"])
        offspring = int(request.form["offspring"])
        pets = int(request.form["pets"])
        sign = int(request.form["sign"])
        smokes = int(request.form["smokes"])
        age = int(le_dict["sc_age"].transform([[request.form["age"]]])[0])
        height = int(le_dict["sc_height"].transform([[request.form["height"]]])[0])
        income = int(le_dict["sc_income"].transform([[request.form["income"]]])[0])
    
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


if __name__ == "__main__":
    app.run()