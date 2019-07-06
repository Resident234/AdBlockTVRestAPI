from flask import Flask, jsonify, request
import json
from database import get_database, Database

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def main():
    with open("db.cnf") as f:
        config = json.load(f)

    # initialize db
    db_cls = get_database(config.get("database_type", None))
    db = db_cls(**config.get("database", {}))
    db.setup()

    if request.method == 'GET':
        return request.args.get('code')
    elif request.method == 'POST':
        json = request.get_json()
        if len(json['code']) == 0:
            return jsonify({'error': 'invalid input'})
        db.return_matches(json['code'])
        return jsonify({'you sent this': json['code']})
    else:
        return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
