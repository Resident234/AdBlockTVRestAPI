from flask import Flask, jsonify, request
#from database import get_database, Database

import json
import pymysql
#import MySQLdb

app = Flask(__name__)

# ec2-3-16-131-11.us-east-2.compute.amazonaws.com db connection config :
# login : root
# password : Po8WuX?v0B9inO6UMOpr

@app.route('/api', methods=['GET', 'POST'])
def main():

    if request.method == 'GET':
        connection = pymysql.connect(host='3.16.131.11',
                                     user='root',
                                     password='Po8WuX?v0B9inO6UMOpr',
                                     db='dejavu',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        '''
        try:
            with connection.cursor() as cursor:
                # SQL
                sql = "SELECT Dept_No, Dept_Name FROM Department "
                # Execute query.
                cursor.execute(sql)
                print("cursor.description: ", cursor.description)
                print()

                for row in cursor:
                    print(row)
        finally:
            # Close connection.
            connection.close()
        '''

        return("connect successful!!")
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
