import json
import os
from flask import Flask, logging, render_template, request
import requests
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.config["API_ADDR"] = 'http://{}'.format(os.environ.get('API_ADDR'))
app.logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
logging.default_handler.setFormatter(os.getenv("LOG_FORMAT", "%(asctime)-15s - %(name)s - %(levelname)s  %(message)s"))


@app.route('/')
def main():
    url = f'{app.config["API_ADDR"]}/get-data/1'
    resp = json.loads(requests.get(url, timeout=3).text)
    return render_template('main.html', data=resp, page=1)


@app.route('/<int:page>')
def next_page(page):
    url = f'{app.config["API_ADDR"]}/get-data/{page}'
    resp = json.loads(requests.get(url, timeout=3).text)
    return render_template('main.html', data=resp, page=page)


@app.route('/<string:datestr>/<int:page>')
def go_date(datestr, page):
    url = f'{app.config["API_ADDR"]}/get-data/{datestr}/{page}'
    resp = json.loads(requests.get(url, timeout=3).text)
    return render_template('date.html', data=resp, page=page)


@app.route('/search/<int:page>', methods=['GET', 'POST'])
def search(page):
    try:
        q = request.form['search']
        startdate = request.form['startdate']
        enddate = request.form['enddate']
        if not q or q == '':
            q = request.args.get('search')
        if not startdate or startdate == '':
            startdate = request.args.get('startdate', '')
        if not enddate or enddate == '':
            enddate = request.args.get('enddate', '')
    except:
        q = request.args.get('search')
        startdate = request.args.get('startdate', '')
        enddate = request.args.get('enddate', '')
    url = f'{app.config["API_ADDR"]}/search/{page}?q={q}&startdate={startdate}&enddate={enddate}'
    resp = json.loads(requests.get(url, timeout=3).text)
    return render_template('search.html', data=resp, page=page, search=q)


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error("Exception occurred on front-end: ", e)
    code = e.code if isinstance(e, HTTPException) else 500
    return render_template("error.html", e=e), code


if __name__ == '__main__':
    for v in ['PORT', 'API_ADDR']:
        if os.environ.get(v) is None:
            print("error: {} environment variable not set".format(v))
            exit(1)

    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
