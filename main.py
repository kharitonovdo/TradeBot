from flask import Flask, render_template, request, redirect
import The_smart_part

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buy', methods=['POST', 'GET'])
def buy():
    if request.method == 'POST':
        try:
            return render_template('buy.html',
                                   result=The_smart_part.main(The_smart_part.dt_now, request.form.get("patern"))[0],
                                   name=The_smart_part.main(The_smart_part.dt_now, request.form.get("patern"))[1])
        except Exception:
            return redirect("abort")
    return render_template('buy.html', result=The_smart_part.main(The_smart_part.dt_now)[0],
                               name=The_smart_part.main(The_smart_part.dt_now)[1])


@app.route('/abort')
def abort():
    return render_template('abort.html')


if __name__ == '__main__':
    app.run(port=60000, host='0.0.0.0')
