def app(environ, start_response):
    """
    (dict, callable( status: str,
                     headers: list[(header_name: str, header_value: str)]))
                  -> body: iterable of strings
    """
    status: '200 OK' 
        headers [ 
            ('Content-Type', 'text/plain')
        ]
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return  body
