# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
#                   encoding="utf8")]

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])