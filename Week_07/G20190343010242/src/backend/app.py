import os
from flask import Flask, jsonify, request
from services.newscomments_svc import NewsCommentsService

app = Flask(__name__)

def __get_comments(page, page_size):
    try:
        newscomments_service = NewsCommentsService()
        results = newscomments_service.get_comments(page=page, page_size=page_size)
        return jsonify(results), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/comments/<int:page>', methods=['GET', 'POST'])
def get_comments_by_page(page):
    if page - 1 < 0:
        page = 1
    return __get_comments(page=page-1, page_size=25)


@app.route('/comments', methods=['GET', 'POST'])
def get_comments():
    return __get_comments(page=None, page_size=None)


@app.route('/comments/<string:date>/<int:page>', methods=['GET', 'POST'])
def get_comments_by_date(date, page):
    try:
        newscomments_service = NewsCommentsService()
        if page - 1 < 0:
            page = 1
        results = newscomments_service.get_comments_by_date(page=page-1, datestr=date)
        return jsonify(results), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/number-of-comments/<string:date>', methods=['GET', 'POST'])
def get_number_of_comments_by_date(date):
    try:
        newscomments_service = NewsCommentsService()
        result = newscomments_service.get_number_of_comments_by_date(date)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/number-of-comments', methods=['GET', 'POST'])
def get_of_comments():
    try:
        newscomments_service = NewsCommentsService()
        result = newscomments_service.get_number_of_comments()
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500

@app.route('/number-of-sentiments', methods=['GET', 'POST'])
def get_number_of_sentiments():
    try:
        newscomments_service = NewsCommentsService()
        result = newscomments_service.get_number_of_sentiments()
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/number-of-sentiments/<string:date>', methods=['GET', 'POST'])
def get_number_of_positive_by_date(date):
    try:
        newscomments_service = NewsCommentsService()
        result = newscomments_service.get_number_of_sentiments_by_date(date)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/search/<int:page>', methods=['GET', 'POST'])
def search_comments(page):
    try:
        newscomments_service = NewsCommentsService()
        q = request.args.get('q', '')
        if page - 1 <= 0:
            page = 1
        result = newscomments_service.search_comments(q, page=page-1)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({'error': ex}), 500


@app.route('/search/<string:datestr>/<int:page>', methods=['GET', 'POST'])
def search_comments_by_date(datestr, page):
    try:
        newscomments_service = NewsCommentsService()
        q = request.args.get('q', '')
        if page - 1 <= 0:
            page = 1
        result = newscomments_service.search_comments_by_date(q, page=page-1, datestr=datestr)
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

    # start Flask server
    # Flask's debug mode is unrelated to ptvsd debugger used by Cloud Code
    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
