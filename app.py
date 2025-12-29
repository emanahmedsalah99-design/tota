from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello! Your Flask app is running in Docker.</h1>"

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"})

if __name__ == "__main__":
    # host='0.0.0.0' is required to make the app accessible outside the container
    app.run(host='0.0.0.0', port=5000)
