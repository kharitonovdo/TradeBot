from flask import Flask, render_template
import The_smart_part

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/invest.html')
def invest():
    return render_template('invest.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
