import pytest
import pandas as pd
from unittest.mock import patch, mock_open
from utils.query_csv import query_joined_data, query_min_group_data
from utils.record_csv import update_count_csv

class TestQueryCSV:
    
    @patch('utils.query_csv.pd.read_csv')
    def test_query_joined_data(self, mock_read_csv):
        """测试查询连接数据功能"""
        # Mock CSV数据
        mock_command_data = pd.DataFrame({
            'id': [1, 2],
            'command_group': ['find_commands', 'grep_commands'],
            'command': ['find /dir -name file', 'grep pattern file'],
            'description': ['查找文件', '搜索模式'],
            'ignore': [None, None]
        })
        mock_count_data = pd.DataFrame({
            'id': [1],
            'command_id': [1],
            'command': ['find /dir -name file'],
            'is_correct': [1]
        })
        mock_read_csv.side_effect = [mock_command_data, mock_count_data]
        
        result = query_joined_data(['find_commands'], 5)
        assert len(result) > 0
        assert 'command' in result[0]

    @patch('utils.query_csv.pd.read_csv')
    def test_query_min_group_data(self, mock_read_csv):
        """测试查询最小组数据功能"""
        mock_command_data = pd.DataFrame({
            'id': [1, 2],
            'command_group': ['find_commands', 'process_commands'],
            'command': ['find /dir', 'ps aux'],
            'description': ['查找', '进程']
        })
        mock_count_data = pd.DataFrame({
            'id': [1],
            'command_id': [1],
            'is_correct': [1]
        })
        mock_read_csv.side_effect = [mock_command_data, mock_count_data]
        
        result = query_min_group_data()
        assert isinstance(result, list)

class TestRecordCSV:
    
    @patch('builtins.open', new_callable=mock_open, read_data='id,command_id,command,is_correct\n1,1,test,1\n')
    def test_update_count_csv(self, mock_file):
        """测试更新计数CSV功能"""
        update_count_csv(1, 'test command', 1)
        mock_file.assert_called()

class TestConfig:
    
    def test_config_values(self):
        """测试配置值"""
        from config import Config
        assert Config.DEBUG is True
        assert Config.PORT == 5001
        assert Config.API_PREFIX == '/api'