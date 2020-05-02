import json
import os
from flask import Flask, jsonify, request
from services.news_comments_svc import NewsCommentsService
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
service = NewsCommentsService()
ok_code = int(os.getenv("OK_CODE", "200"))


def __handle_page(page):
    if page - 1 <= 0:
        page = 1
    return page - 1


@app.route('/search/<int:page>', methods=['GET', 'POST'])
def search_comments(page):
    q = request.args.get('q', '')
    startdate = request.args.get('startdate')
    enddate = request.args.get('enddate')
    result = service.search_comments(q, page=__handle_page(page), startdate=startdate, enddate=enddate)
    return jsonify(result), ok_code


@app.route('/get-data/<int:page>', methods=['GET', 'POST'])
def get_data(page):
    result = service.get_data(page=__handle_page(page))
    return jsonify(result), ok_code


@app.route('/get-data/<string:date>/<int:page>', methods=['GET', 'POST'])
def get_data_by_date(date, page):
    result = service.get_data_by_date(page=__handle_page(page), datestr=date)
    return jsonify(result), ok_code


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error("Exception occurred on restful service: ", e)
    if isinstance(e, HTTPException):
        resp = e.get_response()
        resp.data = json.dumps({'code': e.code, 'name': e.name, 'description': e.description})
        return resp
    else:
        return jsonify({'error': e}), 500


if __name__ == '__main__':
    for v in ['PORT', 'DB_ADDR', "DB_USER", "DB_PASS"]:
        if os.environ.get(v) is None:
            print("error: {} environment variable not set".format(v))
            exit(1)

    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
