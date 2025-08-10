import requests
import json

BASE_URL = 'http://localhost:5001/api'

def test_get_categories():
    """测试获取分类接口"""
    response = requests.get(f'{BASE_URL}/categories')
    print(f"GET /api/categories: {response.status_code}")
    if response.status_code == 200:
        try:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except:
            print(response.text)
    else:
        print(f"错误响应: {response.text}")
    print("-" * 50)

def test_get_commands(category='find_commands'):
    """测试获取命令接口"""
    response = requests.get(f'{BASE_URL}/commands/{category}')
    print(f"GET /api/commands/{category}: {response.status_code}")
    if response.status_code == 200:
        try:
            data = response.json()
            if data['success']:
                print(f"返回 {len(data['commands'])} 条命令")
                if data['commands']:
                    print(f"第一条: {data['commands'][0]['command']}")
            else:
                print(f"错误: {data['error']}")
        except:
            print(response.text)
    else:
        print(f"错误响应: {response.text}")
    print("-" * 50)

def test_random_commands():
    """测试随机命令接口"""
    response = requests.get(f'{BASE_URL}/commands/random')
    print(f"GET /api/commands/random: {response.status_code}")
    if response.status_code == 200:
        try:
            data = response.json()
            if data['success']:
                print(f"返回 {len(data['commands'])} 条随机命令")
            else:
                print(f"错误: {data['error']}")
        except:
            print(response.text)
    else:
        print(f"错误响应: {response.text}")
    print("-" * 50)

def test_record_answer():
    """测试记录答案接口"""
    test_data = {
        'command_id': 102,
        'command': 'grep keyword filename',
        'is_correct': True
    }
    response = requests.post(f'{BASE_URL}/record', json=test_data)
    print(f"POST /api/record: {response.status_code}")
    if response.status_code == 200:
        try:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except:
            print(response.text)
    else:
        print(f"错误响应: {response.text}")
    print("-" * 50)

if __name__ == '__main__':
    print("开始测试后端API...")
    print("=" * 50)
    
    try:
        test_get_categories()
        test_get_commands('find_commands')
        test_get_commands('docker_basic_commands')
        test_random_commands()
        test_record_answer()
        print("✅ 所有测试完成")
    except requests.exceptions.ConnectionError:
        print("❌ 连接失败，请确保后端服务器已启动 (python app.py)")
    except Exception as e:
        print(f"❌ 测试失败: {e}")