from flask import Flask, send_file, request
from main import answer

app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def index():
    return send_file('index.html')


@app.route('/input', methods=['POST'])
def answer_question():
    return answer('da')


@app.route('/<static_file>', methods=['GET'])
def return_js(static_file):
    return send_file(static_file)


if __name__ == '__main__':
    app.run()
