# adhs
Ad-hoc light weight SPARQL endpoint from a file, using Python Flask and RDFLib

## Details
Sometimes one needs to set up a quick SPARQL endpoint for a local Turtle file without installing a triplestore. This is a quick *demo* how to use the Python 3 microframework [Flask](http://flask.pocoo.org/) and [RDFLib](https://github.com/RDFLib) to provide an **Ad-Hoc SPARQL** endpoint based on a Turtle or RDF/XML file.

### Usage

Example:
```
./adhs.py file.ttl -i turtle -p 5000
```

The `-i` parameter is optional but should be used to specify the format of the file. If it's missing, `rdflib.util.guess_format()` will be used.

The `-p` parameter is optional as well. If not provided, flask will be accessible on default port 5000. Navigate to

```
http://localhost:5000/sparql
```

to get a very basic form to enter and submit your queries (the form is just some icing on the cake).

Additionally, the SPARQL endpoint accepts GET requests:

```
http://localhost:5000/sparql?query=select distinct ?s where { ?s a ?c }
```

The answer format will always be JSON, there is no content negotiation at the moment but will probably be implemented in the future.

### Use case

One use case behind the **adhs** was to provide a quick possibility to set up different ontologies to test them with the [Visual SPARQL Builder (VSB)](https://github.com/leipert/vsb) without having them to load into a triplestore like Virtuoso. Additionally, since the VSB needs SPARQL 1.1, it is a convenient alternative on systems don't have high enough version of Virtuoso installed.

### Fun facts

ADHS is actually the German abbreviation for ADHD.

## Future Work

moved to [TODO.md](TODO.md)


