import subprocess
import json
from pathlib import Path
from invoke import task
import requests
from flask import Flask, request, send_from_directory


QUERY_URL = 'http://localhost:8080/query'


app = Flask(__name__)
site = Path('static')


@app.route('/query', methods=['POST'])
def query():
    query = request.get_data().decode('utf8')
    res = requests.post(QUERY_URL, query)
    nice_output = json.dumps(res.json(), indent=2)
    return nice_output


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    filepath = site / path

    if filepath.is_dir():
        index_path = filepath / 'index.html'
        if index_path.exists():
            return send_from_directory(str(site), 'index.html')

    if filepath.exists():
        return send_from_directory(str(site), path)

    return 'Page not found', 404


@task
def serve(ctx):
    app.run(port=8000)


@task
def db(ctx):
    start_dgraph()


@task
def populate(ctx):
    with open('initial-data.txt') as fp:
        res = requests.post(QUERY_URL, fp.read())
        print(res.json())


def start_dgraph():
    subprocess.call('dgraph --schema demo.schema', shell=True)
