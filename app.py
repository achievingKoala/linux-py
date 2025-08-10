from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from query_csv import query_joined_data, query_min_group_data
from record_csv import update_count_csv

app = Flask(__name__)
CORS(app)

@app.route('/api/commands/<category>')
def get_commands(category):
    try:
        if category == 'random':
            categories = query_min_group_data()
            if categories:
                random_category = random.choice(categories)
                commands = query_joined_data([random_category], 5)
            else:
                commands = []
        else:
            commands = query_joined_data([category], 10)
        
        return jsonify({'success': True, 'commands': commands})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/categories')
def get_categories():
    try:
        categories = query_min_group_data()
        return jsonify({'success': True, 'categories': categories})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/record', methods=['POST'])
def record_answer():
    try:
        data = request.json
        update_count_csv(data['command_id'], data['command'], 1 if data['is_correct'] else 0)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)