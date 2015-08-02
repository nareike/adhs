#!/usr/bin/env python
from flask import Flask, request, render_template, redirect
from flask.ext.cors import CORS
from flask_negotiate import consumes, produces
from adhs_response import *
import rdflib
import argparse

# command line parameters
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-p', '--port', default=5000, type=int)
parser.add_argument('-i', '--input', default='guess', choices=[
        'html',
        'hturtle',
        'mdata',
        'microdata',
        'n3',
        'nquads',
        'nt',
        'rdfa',
        'rdfa1.0',
        'rdfa1.1',
        'trix',
        'turtle',
        'xml'
    ], help='Optional input format')

args = parser.parse_args()

# doesn't seem right to include */* ?
_FORMATS = ['*/*', 'text/html', 'application/sparql-results+json', 'application/sparql-results+xml']

# new graph
g = rdflib.Graph()

# parse file into graph
with open(args.file, 'r') as fi:
    if args.input == 'guess':
        fo = rdflib.util.guess_format(args.file)
    else:
        fo = args.input

    g.parse(fi, format=fo)

# set up a micro service using flash
app = Flask(__name__, static_url_path='')
app.debug = True
cors = CORS(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect('/sparql')

@app.route("/sparql", methods=['GET'])
@produces(*_FORMATS)
def sparql_get():
    if 'query' in request.args:
        content = content_override(request.args)
        if content == None:
            content = get_pref_content_type(request)
        qres = g.query(request.args['query'])
        return get_response(qres, content)
    else:
        return render_template('sparql.html', src=args.file, port=request.host)

@app.route("/sparql", methods=['POST'])
@consumes('application/x-www-form-urlencoded')
@produces(*_FORMATS)
def sparql_post():
    if 'query' in request.form:
        content = content_override(request.form)
        if content == None:
            content = get_pref_content_type(request)
        qres = g.query(request.form['query'])
        return get_response(qres, content)
    else:
        return render_template('sparql.html', src=args.file, port=request.host)

def content_override(args):
    if 'format' in args:
        return args['format']
    elif 'output' in args:
        return args['output']
    else:
        return None

def get_pref_content_type(request):
    # exclude */* from FORMATS
    best = request.accept_mimetypes.best_match(_FORMATS[1:])
    # with no clear preference, always return text/html
    if request.accept_mimetypes[best] > request.accept_mimetypes['text/html']:
        return best
    else:
        return 'text/html'

if __name__ == "__main__":
    app.run(port=args.port)

