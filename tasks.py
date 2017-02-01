import subprocess
import json
from invoke import task
import requests


@task
def serve(ctx):
    pass


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
