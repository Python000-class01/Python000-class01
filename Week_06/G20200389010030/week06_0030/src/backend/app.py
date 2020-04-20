import os
from flask import Flask, jsonify
from services.sentiment_svc import SentimentService

app = Flask(__name__)


def __top_sentiments(page_size):
    sentiment_service = SentimentService()
    results = sentiment_service.top_sentiments(page_size)
    return jsonify(results), 200


@app.route('/top_sentiments/<int:page_size>', methods=['GET', 'POST'])
def top_sentiments_custom_page_size(page_size):
    return __top_sentiments(page_size)


@app.route('/top_sentiments', methods=['GET', 'POST'])
def top_sentiments():
    return __top_sentiments(10)


if __name__ == '__main__':
    for v in ['PORT', 'DB_ADDR', "DB_USER", "DB_PASS"]:
        if os.environ.get(v) is None:
            print("error: {} environment variable not set".format(v))
            exit(1)

    # start Flask server
    # Flask's debug mode is unrelated to ptvsd debugger used by Cloud Code
    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
