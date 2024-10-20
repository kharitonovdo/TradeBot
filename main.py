from flask import Flask, render_template
import The_smart_part

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buy')
def buy():
    return render_template('buy.html', result=The_smart_part.main(The_smart_part.dt_now))





if __name__ == '__main__':
    app.run(port=60000, host='0.0.0.0')
