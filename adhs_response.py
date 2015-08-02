from flask import Response, render_template, Markup

def get_response(qres, output):
    if output == 'application/sparql-results+json':
        return Response(
                qres.serialize(format='json').decode('utf-8'),
                content_type='application/sparql-results+json'
                )
    elif output == 'text/html':
        return render_template('response.html', tabledata=Markup(html_serialize(qres)))
    elif output == 'application/sparql-results+xml':
        return Response(
                qres.serialize(format='xml').decode('utf-8'),
                content_type='application/sparql-results+xml')

    else:
        return None

def html_serialize(result):
    '''
    Outputs the result of a rdflib.query
    '''

    output = '    <tr>\n'
    for v in result.vars:
        output += '        <th>%s</th>\n' % v
    output += '    </tr>\n'

    for row in result:
        output += '    <tr>\n'
        for val in row:
            output += '        <td>%s</td>\n' % (val if (val != None) else '')
        output += '    </tr>'
    return output
