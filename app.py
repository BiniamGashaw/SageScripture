from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World, from Flask, niggas is gay!"

if __name__ == "__main__":
    app.run(debug=True)