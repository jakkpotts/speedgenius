from flask import Flask, request, jsonify, render_template
from gpt import send_message

app = Flask(__name__, static_folder='static')

# Route to handle both GET (serving the form) and POST (processing the query)
@app.route('/genius', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Access POST data (JSON format expected)
        data = request.get_json()  # For JSON data
        query = data.get("query")
        
        if not query:
            return jsonify({"error": "No query provided"}), 400
        
        try:
            # Process the query (using your send_message function)
            result = send_message(query)
            return jsonify({"message": result})
        except Exception as e:
            return jsonify({"error": f"Error processing query: {str(e)}"}), 500

    elif request.method == 'GET':
        # If it's a GET request to serve the form, render the genius.html template
        return render_template('genius.html')

if __name__ == '__main__':
    app.run(debug=True)