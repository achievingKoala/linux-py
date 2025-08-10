"""
配置文件
"""
import os

class Config:
    # Flask配置
    DEBUG = os.environ.get('FLASK_ENV') != 'production'
    PORT = int(os.environ.get('PORT', 5001))
    HOST = os.environ.get('HOST', '0.0.0.0')
    
    # 数据文件路径
    COMMAND_DATA_PATH = 'csv/command_data.csv'
    COUNT_DATA_PATH = 'csv/count.csv'
    
    # API配置
    API_PREFIX = '/api'
    
    # CORS配置
    CORS_ORIGINS = ['*']
    
    # 默认查询限制
    DEFAULT_LIMIT = 10
    RANDOM_LIMIT = 5