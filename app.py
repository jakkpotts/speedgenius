from flask import Flask, request, jsonify
from gpt import send_message

app = Flask(__name__)

@app.route('/genius', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        # Access POST data
        data = request.get_json()  # For JSON data
        # Uncomment if expecting form or raw data instead
        # data = request.form       # For form data
        # data = request.data       # For raw data

        # Process and respond to POST request
        result = {"message": "Received your data!", "data": data}
        return jsonify(result)

    elif request.method == 'GET':
        # Access GET parameters
        query_param = request.args.get('query', '')  # Default to '' if 'query' is not provided
        if query_param:
            response = send_message(query_param)
            return jsonify(response)
        return jsonify("success")

if __name__ == '__main__':
    app.run(debug=True)