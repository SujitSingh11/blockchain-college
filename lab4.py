from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/sujit')
def sujit():
    return 'Hello sujit'


app.run(host='localhost', port=5000)
