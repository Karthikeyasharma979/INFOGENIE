from flask import Flask, request, jsonify
from flask_cors import CORS
import ai
app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400
        message = data["message"]
        response_text = ai.process_ai_analysis(message)
        return jsonify({"response": response_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=3000, debug=True)
