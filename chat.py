#!/bin/env python
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    # as it is self-signed certificates the browser will generate a security warning
    socketio.run(app, ssl_context=('cert.pem', 'key.pem'))
