from flask import Flask, jsonify, request
app = Flask(__name__)

result = [
    {
        'id': 1,
        'code': "default code"
    }
]


@app.route("/api/v1.0/s/", methods=['POST'])
def hello():
    return jsonify({'result': request})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
