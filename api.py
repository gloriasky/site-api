from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_simple import (
    JWTManager
)
from waitress import serve

import contacts, projects

app = Flask(__name__)
CORS(app, supports_credentials=True, expose_headers='Content-Disposition')
jwt = JWTManager(app)


@app.route('/api/contact-links')
def get_contacts():
    try:
        return jsonify(contacts.get_links()), 200
    except Exception as e:
        return 'Failed to get contacts: ' + str(e), 400


@app.route('/api/projects')
def get_projects():
    try:
        return jsonify(projects.get_projects()), 200
    except Exception as e:
        return 'Failed to get projects: ' + str(e), 400


@app.route('/api/projects/create', methods=['POST'])
def create_project():
    try:
        project = request.json
        projects.save_project(project)
        return 'Success', 200
    except Exception as e:
        return 'Failed to get projects: ' + str(e), 400


if __name__ == "__main__":
    serve(app, port=5000)
