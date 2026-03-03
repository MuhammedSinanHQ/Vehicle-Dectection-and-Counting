import os
from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='app/templates')

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)