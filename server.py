from flask import Flask, jsonify, request
from database import get_database, Database

import json

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def main():

    if request.method == 'GET':

        #with open("db.cnf") as f:
        #    config = json.load(f)

        # initialize db
        #db_cls = get_database(config.get("database_type", None))
        #db = db_cls(**config.get("database", {}))
        #db.setup()

        return request.args.get('code')
    elif request.method == 'POST':
        json_local = request.get_json()
        if len(json_local['code']) == 0:
            return jsonify({'error': 'invalid input'})
        #db.return_matches(json['code'])
        return jsonify({'you sent this': json_local['code']})
    else:
        return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
