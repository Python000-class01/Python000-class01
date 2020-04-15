from flask import render_template
from app import app
from models import BooKComments


@app.route('/')
def index():
    shorts = BooKComments.query.all()[0:10]
    return render_template('index.html', shorts=shorts)


if __name__ == '__main__':
    app.run(debug=True)