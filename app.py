import sys
import signs
from flask import Flask, request, jsonify, redirect
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)

reload(sys)
sys.setdefaultencoding('utf-8')


class API(Resource):
    def get(self):
        return redirect("https://aztro.readthedocs.io/en/latest/", code=302)

    def post(self):
        sign = request.args.get('sign')
        day = request.args.get('day')
        timezone = request.args.get('tz')
        response = signs.getData(sign=sign, day=day, tz=timezone)
        try:
            return response
        except:
            print "error"


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=404, text=str(e)), 404


api.add_resource(API, '/')

if __name__ == '__main__':
    app.run(debug=False)
