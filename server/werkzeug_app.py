#!/usr/bin/env python3
from werkzeug.wrappers.base import Request, Response
from werkzeug.serving import run_simple
@Request.application
def application(request):
    response = Response('A WSGI generated this response!')
    print(f'This web server is running at {request.remote_addr}')
    return response

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=5555,
        application=application,
        use_reloader=True  # Optional: Enables auto-reloading for development
    )
