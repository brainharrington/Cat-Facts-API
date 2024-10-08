import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Function to get a cat fact from the external API
def get_cat_fact():
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        fact = response.json()["fact"]
        return fact
    else:
        return "Error fetching cat fact."

# API endpoint to return a cat fact
@app.route('/catfact', methods=['GET'])
def cat_fact():
    fact = get_cat_fact()
    return jsonify({'fact': fact})

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
