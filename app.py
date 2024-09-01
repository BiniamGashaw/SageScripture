from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI


app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

client = OpenAI(
    api_key='anything',
    base_url="http://localhost:3040/v1/"
)

@app.route("/ask", methods=['POST'])
def ask_openai():
    data = request.json
    user_message = data.get('message', '')

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message},
            ],
        )
        response = completion.choices[0].message.content
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)