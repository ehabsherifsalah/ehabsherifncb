from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', consultant=data['consultant'], projects=data['projects'], offers=data.get('offers', []))

@app.route('/projects')
def projects():
    data = load_data()
    return render_template('projects.html', consultant=data['consultant'], projects=data['projects'])

@app.route('/contact')
def contact():
    data = load_data()
    return render_template('contact.html', consultant=data['consultant'])

@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    data = load_data()
    project = next((p for p in data['projects'] if p['id'] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({"error": "Project not found"}), 404

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    # Mock subscription logic for lead generation
    return jsonify({"success": "Subscription successful. You will receive the latest offers via push notifications!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
