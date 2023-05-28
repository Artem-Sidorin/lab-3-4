from flask import Flask, render_template, request
import calc

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        try:
            summ = int(request.form.get('summ'))
            period = int(request.form.get('period'))
            percent = int(request.form.get('percent'))
        except ValueError:
            summ = 0
            period = 0
            percent = 0
        choose = int(request.form['typ'])
        if choose == 1:
            result = calc.ann_result(summ, period, percent)
        else:
            result = calc.diff_result(summ, period, percent)
    return render_template('index.html', m_payment=result[0], deb_perc=result[1],
                           total=result[2])


if __name__ == '__main__':
    app.run()