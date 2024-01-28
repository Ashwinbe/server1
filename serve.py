from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route to handle form submissions
@app.route('/save', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        password = data['password']

        # Create a dictionary with the form data
        form_data = {'name': name, 'email': email, 'password': password}

        # Load existing data from JSON file
        try:
            with open('data.json', 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        # Append new form data to existing data
        existing_data.append(form_data)

        # Save the updated data back to the JSON file
        with open('data.json', 'w') as file:
            json.dump(existing_data, file, indent=2)

        return jsonify({'message': 'Data received successfully!'}), 200

    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to process the request.'}), 500

# New route for the root URL
@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
