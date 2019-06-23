from flask import Flask, jsonify, request
app = Flask(__name__)

result = [
    {
        'id': 1,
        'code': "default code"
    }
]


@app.route('/api', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return 'GET'
    elif request.method == 'POST':
        return jsonify({'result': request})
    else:
        return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
