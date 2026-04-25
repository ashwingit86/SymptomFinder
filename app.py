from flask import Flask, request, jsonify

app = Flask(__name__)

symptom_db = {
    "fever": ["Flu", "COVID-19", "Infection"],
    "headache": ["Migraine", "Stress", "Dehydration"],
    "cough": ["Cold", "Bronchitis", "Asthma"],
}

def find_conditions(symptoms):
    conditions = []
    for s in symptoms:
        if s.lower() in symptom_db:
            conditions.extend(symptom_db[s.lower()])
    return list(set(conditions))

def generate_advice(conditions):
    if not conditions:
        return "No major condition detected. Monitor symptoms."
    return "If symptoms persist for more than 3 days, consult a doctor."

@app.route("/")
def home():
    return "Symptom Information Finder Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    symptoms = data.get("symptoms", [])

    conditions = find_conditions(symptoms)
    advice = generate_advice(conditions)

    return jsonify({
        "symptoms": symptoms,
        "possible_conditions": conditions,
        "advice": advice,
        "disclaimer": "This is general information only, not medical advice."
    })

if __name__ == "__main__":
    app.run(debug=True)