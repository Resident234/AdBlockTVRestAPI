from flask import Flask, jsonify, request
# from database import get_database, Database

import json
import pymysql
# import MySQLdb
from collections import defaultdict

from dejavu import Dejavu
import dejavu.logger as logger
import ast


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
        array_hashes = file_log.readlines()
    elif request.method == 'POST':
        json_local = request.get_json()
        if len(json_local['hashes']) == 0:
            return jsonify({'error': 'invalid input'})

        string_hashes = json_local['hashes']
        string_hashes = string_hashes.replace("[", "")
        string_hashes = string_hashes.replace("]", "")
        array_hashes = string_hashes.rstrip().split(', ')

    hashes = dict()
    samples_indexes = []
    for string_hash in array_hashes:
        sample_index, hash_local, offset = string_hash.rstrip().split('|')
        if sample_index in hashes:
            hashes[sample_index].append((hash_local, int(offset)))
        else:
            hashes[sample_index] = []
        if sample_index not in samples_indexes:
            samples_indexes.append(sample_index)

    matches = []
    for sample_index in samples_indexes:
        matches.extend(djv.rest_find_matches(hashes[sample_index]))
    return jsonify(djv.align_matches(matches))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
