from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from config import Config
from utils.query_csv import query_joined_data, query_min_group_data
from utils.record_csv import update_count_csv

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=Config.CORS_ORIGINS)

@app.route(f'{Config.API_PREFIX}/commands/<category>')
def get_commands(category):
    """获取指定类别的命令"""
    try:
        if category == 'random':
            categories = query_min_group_data()
            if categories:
                random_category = random.choice(categories)
                commands = query_joined_data([random_category], Config.RANDOM_LIMIT)
            else:
                commands = []
        else:
            commands = query_joined_data([category], Config.DEFAULT_LIMIT)
        
        return jsonify({
            'success': True, 
            'commands': commands,
            'category': category,
            'count': len(commands)
        })
    except Exception as e:
        app.logger.error(f'Error getting commands for category {category}: {str(e)}')
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route(f'{Config.API_PREFIX}/categories')
def get_categories():
    """获取所有可用的命令类别"""
    try:
        categories = query_min_group_data()
        return jsonify({
            'success': True, 
            'categories': categories,
            'count': len(categories)
        })
    except Exception as e:
        app.logger.error(f'Error getting categories: {str(e)}')
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route(f'{Config.API_PREFIX}/record', methods=['POST'])
def record_answer():
    """记录用户答题结果"""
    try:
        data = request.json
        if not data or 'command_id' not in data or 'command' not in data or 'is_correct' not in data:
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
            
        update_count_csv(
            data['command_id'], 
            data['command'], 
            1 if data['is_correct'] else 0
        )
        return jsonify({
            'success': True,
            'message': 'Answer recorded successfully'
        })
    except Exception as e:
        app.logger.error(f'Error recording answer: {str(e)}')
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route(f'{Config.API_PREFIX}/health')
def health_check():
    """健康检查接口"""
    return jsonify({
        'status': 'healthy',
        'service': 'Linux Command Learning API'
    })

if __name__ == '__main__':
    app.run(
        debug=Config.DEBUG, 
        host=Config.HOST, 
        port=Config.PORT
    )