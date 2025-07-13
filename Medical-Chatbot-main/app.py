from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests from your React app

@app.route('/get-diagnosis', methods=['POST'])
def get_diagnosis():
    data = request.get_json()

    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    symptoms = data.get('symptoms')
    days = int(data.get('days'))

    # Use your existing logic here — modify your `tree_to_code` and `sec_predict` to be callable
    # For now, return dummy response:
    return jsonify({
        "name": name,
        "possibleDiseases": ["Flu", "Common Cold"],
        "precautions": ["Rest", "Drink Water", "See a Doctor"],
        "advice": "Consult a doctor if symptoms persist.",
    })

if __name__ == '__main__':
    app.run(debug=True)
