import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 设置工作目录为脚本所在目录
print(os.getcwd())

import pandas as pd

def read_csv_files():
    try:
        docker_data = pd.read_csv('csv/dockerData.csv')
        count_data = pd.read_csv('csv/count.csv')
        return docker_data, count_data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None
    except pd.errors.EmptyDataError:
        print("Error: One of the files is empty.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

docker_data, count_data = read_csv_files()

if docker_data is not None:
    print("Docker Data:")
    print(docker_data.head())

if count_data is not None:
    print("Count Data:")
    print(count_data.head())

if docker_data is not None and count_data is not None:
    # Merge the two DataFrames on 'id' and 'command_id'
    merged_data = pd.merge(docker_data, count_data, left_on='id', right_on='command_id', how='left')
    
    # Count occurrences of each 'id'
    # id_counts = merged_data['id'].value_counts()
    
    # Print the counts
    # print("ID Occurrences:")
    print(merged_data)



