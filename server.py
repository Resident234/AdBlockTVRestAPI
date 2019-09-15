from flask import Flask, jsonify, request
#from database import get_database, Database

import json
import pymysql
#import MySQLdb

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
    '''
    connection = pymysql.connect(host='3.16.131.11',
                                 user='root',
                                 password='Po8WuX?v0B9inO6UMOpr',
                                 db='dejavu',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)'''
    if request.method == 'GET':
        return "count records in db: %s" % djv.get_num_songs()
    elif request.method == 'POST':
        json_local = request.get_json()
        if len(json_local['code']) == 0:
            return jsonify({'error': 'invalid input'})

        matches = []
        matches.extend(djv.find_hashes(json['code']))
        return jsonify({'result': djv.align_matches(matches)})

        #return jsonify({'you sent this': json_local['code']})
    else:
        return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
