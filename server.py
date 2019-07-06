from flask import Flask, jsonify, request
import logging

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
        return request.args.get('code')
    elif request.method == 'POST':
        return request.args.get('code')
    else:
        return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
