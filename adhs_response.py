from flask import Response

def get_response(qres, output):
    if output == 'json':
        return Response(
                qres.serialize(format='json').decode('utf-8'),
                content_type="application/json"
                )
    elif output == 'html':
        return Response(
                html_serialize(qres),
                content_type="text/html"
                )
    elif output == 'xml':
        return Response(
                qres.serialize(format='xml').decode('utf-8'),
                content_type="application/xml"
                )
    else:
        return None

def html_serialize(result):
    '''
    Outputs the result of a rdflib.query
    '''

    output  = '<table border="1">\n'
    output += '    <tr>\n'
    for v in result.vars:
        output += '        <th>%s</th>\n' % v
    output += '    </tr>\n'

    for row in result:
        output += '    <tr>\n'
        for val in row:
            output += '        <td>%s</td>\n' % val
        output += '    </tr>\n'
    output += '</table>\n'

    return output
