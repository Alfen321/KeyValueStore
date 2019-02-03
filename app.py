from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api, request
import db
# import json


app = Flask(__name__)
api = Api(app)


def main():
    # Remove debug=True to disable auto reload on code change + on release!
    app.run(debug=False, host='0.0.0.0', port=5000)


@app.route('/')
def index():
    return render_template('index.html')


# uses post instead of a get because I can't get xhttpRequest to have a body on a get
class database_get(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        data = {}
        key = json_data['key']
        val = db.db_get(key)
        if val is not None:
            data[key] = val
        return jsonify(data)


class database_set(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        data = {}
        db.db_set(json_data['key'], json_data['value'])
        return jsonify(data)


class offset(Resource):
    def get(self):
        data = db.offsets_get()
        return jsonify(data)

class reload_offset(Resource):
    def get(self):
        data = db.reload_offset_memory()
        return jsonify(data)


api.add_resource(database_set, '/set')
api.add_resource(database_get, '/get')
api.add_resource(offset, '/offset')
api.add_resource(reload_offset, '/offset/reload')
