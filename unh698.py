from flask import Flask, render_template
app = Flask(__name__)

from prometheus_metrics import setup_metrics
setup_metrics(app)

@app.route('/')
def mainRoute():
    return render_template('hello.html')

@app.route('/boring1')
def boring1():
    return render_template('boring1.html')

@app.route('/boring2')
def boring2():
    return render_template('boring2.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)




