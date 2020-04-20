import json
import os
from flask import Flask, render_template, redirect, url_for, request, jsonify
import requests

app = Flask(__name__)
app.config["TOP_SENTIMENTS"] = 'http://{}/top_sentiments'.format(os.environ.get('API_ADDR'))


@app.route('/')
def main():
    if request.args.lists():
        page_size = request.args.to_dict().get('pageSize', 10)
    else:
        page_size = 10
    url = f'{app.config["TOP_SENTIMENTS"]}/{page_size}'
    response = requests.get(url, timeout=3)
    json_response = json.loads(response.text)
    item_name = json_response[0]['item_name']
    return render_template('home.html', page_size=page_size, item_name=item_name, results=json_response)


@app.route('/post', methods=['POST'])
def post():
    page_size = request.form['pageSize']
    return redirect(f"{url_for('main')}?pageSize={page_size}")


if __name__ == '__main__':
    for v in ['PORT', 'API_ADDR']:
        if os.environ.get(v) is None:
            print("error: {} environment variable not set".format(v))
            exit(1)

    #start Flask server
    #Flask's debug mode is unrelated to ptvsd debugger used by Cloud Code
    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
