# DGraph Quickstart

## Installation

Install dgraph:

```
curl https://get.dgraph.io > /tmp/get.sh
less /tmp/get.sh
sh /tmp/get.sh
```

Install Flask and other Python dependencies:

```
mkvirtualenv -p python3 dgraph
pip install -r requirements.txt
```

If you're using Atom, install the language-graphql package.

## Start database

```
inv db
```

## Load example data

When the database is running, run

```
inv download_example_data
inv load_example_data
```

## Sources

- [Dgraph installation](https://wiki.dgraph.io/Get_Started#Step_1:_Installation)
- [Load dataset](https://wiki.dgraph.io/Get_Started#Load_dataset)
