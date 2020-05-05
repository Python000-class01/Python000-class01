from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello word!'

@app.route('/hell')
def hell():
    return render_template('index.html', text='Welcome ！')

@app.route('/table')
def table():
    # shorts = [['1','红楼梦','shorts','0.999999'],
    #         ['2','红楼梦','shorts','0.321'],
    #         ['3','红楼梦','shorts','0.32'],
    #         ['4','三体','shorts','0.31231']]
    shorts = T1.query.all()[0:10]
    return render_template('table.html', shorts=shorts)

if __name__ == "__main__":
    app.run(debug=True)