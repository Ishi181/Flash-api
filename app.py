from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded user information
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def post_data():
    data = request.json.get('data', [])
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha() and len(item) == 1]
    
    highest_alphabet = []
    if alphabets:
        highest_char = max(alphabets, key=lambda x: x.upper())
        highest_alphabet.append(highest_char)

    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)