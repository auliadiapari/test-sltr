from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return f"Anonymous"

@app.route('/welcome/<nama>')
def welcome_nama(nama):
    return f"Selamat datang {nama}"

@app.route('/health')
def health():
    status = {"status": "OK"}
    return jsonify(status), 200

@app.route('/liveness')
def liveness():
    status = {"status": "OK"}
    return jsonify(status), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)