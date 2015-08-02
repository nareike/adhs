# adhs
Ad-hoc light weight SPARQL endpoint from a file, using Python Flask and RDFLib

## Details
Sometimes one needs to set up a quick SPARQL endpoint for a local Turtle file without installing a triplestore. This is a quick *demo* how to use the Python 3 microframework [Flask](http://flask.pocoo.org/) and [RDFLib](https://github.com/RDFLib) to provide an **Ad-Hoc SPARQL** endpoint based on a Turtle or RDF/XML file.

## Installation

adhs requires python > 3. You can install dependencies with `pip`:

```
pip install -r requirements.txt
```

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

Additionally, the SPARQL endpoint accepts GET and POST requests.

Example of a GET request via URL:

```
http://localhost:5000/sparql?query=select distinct ?s where { ?s a ?c }&format=<CONTENT-TYPE>
```

The `format` has to be specified via the _accept type_ (see below) but in future there might be more fine-grained options.

_Note:_ Instead of `format`, the parameter `output` can be used as well.

Example with cURL:

```
curl -d "query=select distinct ?c where {?s a ?c}" \
     -H "Accept: text/html" \
     localhost:5000/sparql
```

The content type has to be `application/x-www-form-urlencoded`, whereas the _accept type_ can be one of the following:

* `text/html`
* `application/sparql-results+json`
* `application/sparql-results+xml`

Additionally, the _accept type_ can also be set with the `format` (or alternatively) `output` parameter.

If no accept type is specified, the default type is `text/html` unless it's overridden with `format` or `output`. When an _accept type_ is set via content negotiation and as well with the `format` or `output` parameter, the parameter takes precedence over the content negotiation.

### Use case

One use case behind the **adhs** was to provide a quick possibility to set up different ontologies to test them with the [Visual SPARQL Builder (VSB)](https://github.com/leipert/vsb) without having to load them into a triplestore like Virtuoso. Additionally, since the VSB needs SPARQL 1.1, it is a convenient alternative on systems don't have high enough version of Virtuoso installed.

### Fun facts

ADHS is actually the German abbreviation for ADHD.

## Future Work

moved to [TODO.md](TODO.md)
