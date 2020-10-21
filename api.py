from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_simple import (
    JWTManager
)
from waitress import serve

import contacts

app = Flask(__name__)
CORS(app, supports_credentials=True, expose_headers='Content-Disposition')
jwt = JWTManager(app)


@app.route('/api/contact-links')
def get_contacts():
    try:
        return jsonify(contacts.get_links()), 200
    except Exception as e:
        return 'Failed to generate new password: ' + str(e), 400


if __name__ == "__main__":
    serve(app, port=5000)
