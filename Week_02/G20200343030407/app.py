from flask import Flask, request, jsonify, Response, render_template
from market996 import User, Goods

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('index.html')


@app.route('/check.do', methods=["POST"])
def check():
    params = request.form
    name_list = params.getlist('name')
    price_list = params.getlist('price')
    count_list = params.getlist('count')
    vip = params.get('vip')
    user = User(vip)
    goods_list = list()
    for name, price, count in zip(name_list, price_list, count_list):
        goods = Goods(name, price, count)
        goods_list.append(goods)
    total, count = user.check(goods_list)
    return render_template('check.html', total=total)


if __name__ == '__main__':
    app.run(host="127.0.0.1")
