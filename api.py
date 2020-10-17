from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_simple import (
    JWTManager
)
from waitress import serve

app = Flask(__name__)
CORS(app, supports_credentials=True, expose_headers='Content-Disposition')
jwt = JWTManager(app)


@app.route('/api/contacts')
def get_contacts():
    try:
        contact = {
            'email': 'valadzkokseniya@gmail.com'
        }
        return jsonify(contact), 200
    except Exception as e:
        return 'Failed to generate new password: ' + str(e), 400


if __name__ == "__main__":
    serve(app, port=5000)
