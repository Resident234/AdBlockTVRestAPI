from flask import Flask, jsonify, request
# from database import get_database, Database

import json
import pymysql
# import MySQLdb
from collections import defaultdict

from dejavu import Dejavu
import dejavu.logger as logger

with open("dejavu.cnf") as f:
    config = json.load(f)

app = Flask(__name__)


# ec2-3-16-131-11.us-east-2.compute.amazonaws.com db connection config :
# login : root
# password : Po8WuX?v0B9inO6UMOpr

@app.route('/api', methods=['GET', 'POST'])
def main():
    djv = Dejavu(config)

    if request.method == 'GET':
        file_log = open("hashes_samples.log", "r")
        fl = file_log.readlines()
        hashes = dict()
        samples_indexes = []
        for string in fl:
            sample_index, hash_local, offset = string.rstrip().split('|')
            if sample_index in hashes:
                hashes[sample_index].append((hash_local, int(offset)))
            else:
                hashes[sample_index] = []
            if sample_index not in samples_indexes:
                samples_indexes.append(sample_index)
        file_log.close()

        matches = []
        for sample_index in samples_indexes:
            matches.extend(djv.rest_find_matches(hashes[sample_index]))

        return str(djv.align_matches(matches))
        return "count records in db: %s" % djv.get_num_songs()
    elif request.method == 'POST':
        json_local = request.get_json()
        f = open("dict.txt", "w")
        f.write(str(json_local))
        f.close()
        if len(json_local['code']) == 0:
            return jsonify({'error': 'invalid input'})

        matches = []
        matches.extend(djv.find_hashes(json['code']))
        return jsonify({'result': djv.align_matches(matches)})

        # return jsonify({'you sent this': json_local['code']})
    else:
        return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
