import os
from flask import Flask, jsonify, request
from services.newscomments_svc import NewsCommentsService

app = Flask(__name__)


@app.route('/search/<int:page>', methods=['GET', 'POST'])
def search_comments(page):
    try:
        newscomments_service = NewsCommentsService()
        q = request.args.get('q', '')
        if page - 1 <= 0:
            page = 1
        startdate = request.args.get('startdate')
        enddate = request.args.get('enddate')
        result = newscomments_service.search_comments(q, page=page-1, startdate=startdate, enddate=enddate)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/get-data/<int:page>', methods=['GET', 'POST'])
def get_data(page):
    try:
        if page - 1 <= 0:
            page = 1
        newscomments_service = NewsCommentsService()
        result = newscomments_service.get_data(page=page-1, page_size=25)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/get-data/<string:date>/<int:page>', methods=['GET', 'POST'])
def get_data_by_date(date, page):
    try:
        if page - 1 <= 0:
            page = 1
        newscomments_service = NewsCommentsService()
        result = newscomments_service.get_data_by_date(page=page-1, page_size=25, datestr=date)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


if __name__ == '__main__':
    for v in ['PORT', 'DB_ADDR', "DB_USER", "DB_PASS"]:
        if os.environ.get(v) is None:
            print("error: {} environment variable not set".format(v))
            exit(1)

    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
