# 集成测试 - API接口测试
import pytest
import json
from app import app

@pytest.fixture
def client():
    """创建测试客户端"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """测试健康检查接口"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_get_categories(client):
    """测试获取类别接口"""
    response = client.get('/api/categories')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'categories' in data

def test_get_commands_valid_category(client):
    """测试获取有效类别的命令"""
    response = client.get('/api/commands/find_commands')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert 'commands' in data

def test_get_random_commands(client):
    """测试获取随机命令"""
    response = client.get('/api/commands/random')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True

def test_record_answer_valid(client):
    """测试记录有效答案"""
    test_data = {
        'command_id': 1,
        'command': 'test command',
        'is_correct': True
    }
    response = client.post('/api/record', 
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True

def test_record_answer_invalid(client):
    """测试记录无效答案"""
    test_data = {'invalid': 'data'}
    response = client.post('/api/record',
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False