#!/usr/bin/env python
from flask import Flask, Response, request, render_template
from flask.ext.cors import CORS
import rdflib
import argparse

# command line parameters
parser = argparse.ArgumentParser()
parser.add_argument('file')
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
cors = CORS(app)

@app.route("/sparql", methods=['GET'])
def sparql():
    if 'query' in request.args:
        query = request.args['query']
        qres = g.query(query)
        return Response(qres.serialize(format='json').decode('utf-8'), content_type="application/json")
    else:
        return render_template('sparql.html', src=args.file, port=request.host)

if __name__ == "__main__":
    app.run()

