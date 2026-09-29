import base64


def check_auth(handler):
    auth_header = handler.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Basic '):
        return False

    encoded_credentials = auth_header.split(' ', 1)[1]
    decoded = base64.b64decode(encoded_credentials).decode('utf-8')
    username, password = decoded.split(':', 1)

    return username == 'admin' and password == 'momo2026'