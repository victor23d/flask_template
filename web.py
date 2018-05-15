from json_out import *
from flask import Flask, request, jsonify, render_template
import core

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/')
def api():
    return 'api/g?p='


@app.route('/api/g', methods=['GET', 'POST'])
def api_g():
    p = request.args.get('p', '')
    # p = request.form['p']
    if p == '':
        return ''
    else:
        j = core.get_json(p)

    return jsonify(j)


@app.route('/table', methods=['GET'])
def table():
    p = request.args.get('p', '')
    url = 'http://localhost/api/g?p=' + p
    s = table_json(url)

    # return table_json('http://localhost/api/g?p=test')
    return s
