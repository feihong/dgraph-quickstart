import subprocess
import signal
import json
from pathlib import Path
import contextlib

from invoke import task
import requests
from flask import Flask, request, send_from_directory


EXAMPLE_DATA_URLS = """\
https://github.com/dgraph-io/benchmarks/blob/master/data/21million.rdf.gz
https://github.com/dgraph-io/benchmarks/blob/master/data/sf.tourism.gz
https://github.com/dgraph-io/benchmarks/blob/master/data/21million.schema""".splitlines()


app = Flask(__name__)
site = Path('static')


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
def download_example_data(ctx):
    for url in EXAMPLE_DATA_URLS:
        filename = Path(url).name
        if not Path(filename).exists():
            subprocess.call(['wget', url, '-O', 'data/' + filename])


@task
def populate(ctx):
    with open('initial-data.txt') as fp:
        res = requests.post(QUERY_URL, fp.read())
        print(res.json())


def start_dgraph():
    subprocess.call('dgraph --schema demo.schema', shell=True)
