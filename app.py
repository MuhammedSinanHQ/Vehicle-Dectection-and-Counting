from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)