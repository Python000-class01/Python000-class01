import json
import os
from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)
app.config["API_ADDR"] = 'http://{}'.format(os.environ.get('API_ADDR'))


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
        if not q or q == '':
            q = request.args.get('search')
    except:
        q = request.args.get('search')
    url = f'{app.config["API_ADDR"]}/search/{page}?q={q}'
    resp = json.loads(requests.get(url, timeout=3).text)
    return render_template('search.html', data=resp, page=page, search=q)


@app.route('/search/<string:date>/<int:page>', methods=['GET', 'POST'])
def search_by_date(date, page):
    try:
        q = request.form['search']
        if not q or q == '':
            q = request.args.get('search')
    except:
        q = request.args.get('search')
    url = f'{app.config["API_ADDR"]}/search/{date}/{page}?q={q}'
    resp = json.loads(requests.get(url, timeout=3).text)
    return render_template('search.html', data=resp, page=page, search=q, date=date)


if __name__ == '__main__':
    for v in ['PORT', 'API_ADDR']:
        if os.environ.get(v) is None:
            print("error: {} environment variable not set".format(v))
            exit(1)

    #start Flask server
    #Flask's debug mode is unrelated to ptvsd debugger used by Cloud Code
    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
