import subprocess
import json
from pathlib import Path
from invoke import task
import requests
from flask import Flask, request, send_from_directory


app = Flask(__name__)
site = Path('static')


@app.route('/query', methods=['POST'])
def query():
    import random
    return '%s %d' % (request.get_data().decode('utf8'), random.randint(1, 100))


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
        res = requests.post('http://localhost:8080/query', fp.read())
        print(res.json())


def start_dgraph():
    subprocess.call('dgraph --schema demo.schema', shell=True)
