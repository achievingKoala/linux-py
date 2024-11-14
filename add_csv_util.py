import pandas as pd
import os
import question
import docker_question
import k8s_question


# for array_name in dir(k8s_question):
#     array = getattr(k8s_question, array_name)
#     if isinstance(array, list):  # Check if the attribute is a list
#         print(f"Array '{array_name}':")
#         for item in array:
#             print(item)
#         print()  # Newline for readability between arrays
# import inspect


def save_commands_to_csv(commands_array, array_name, file_path='csv/command_data.csv'):
    import csv
    import os
    
    # Get the next ID
    start_id = 1
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            existing_ids = [int(row[0]) for row in reader if row]
            if existing_ids:
                start_id = max(existing_ids) + 1
    
    # Write or append to CSV
    mode = 'a' if os.path.exists(file_path) else 'w'
    with open(file_path, mode=mode, newline='') as file:
        writer = csv.writer(file)
        if mode == 'w':  # Only write header for new file
            writer.writerow(['id', 'command_group', 'command', 'description'])
        
        for idx, command in enumerate(commands_array, start_id):
            writer.writerow([
                idx,
                array_name,
                command['command'],
                command['description']
            ])

# Loop through all attributes in k8s_question to find arrays
# for name, value in inspect.getmembers(k8s_question):
#     if isinstance(value, list):  # Check if the attribute is a list
#         print(f"Array '{name}':")
#         print(f"Value '{value}'")
#         # save_commands_to_csv(value, name)
#         for item in value:
#             print(item)
#         print()  # Newline for readability between arrays


# Example usage with docker_swarm_commands
save_commands_to_csv(docker_question.docker_advance_commands, 'docker_advance_commands')

def add_data(new_data, file_path="csv/command_data.csv"):
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 读取已存在的数据
        df = pd.read_csv(file_path)
        
        # 找到现有数据的最大 id
        max_id = df["id"].max() if "id" in df.columns else 0
    else:
        # 如果文件不存在，初始化一个空的 DataFrame
        df = pd.DataFrame(columns=["id", "name", "age"])
        max_id = 0

    # 将新数据转为 DataFrame 并添加自增 id 列
    new_df = pd.DataFrame(new_data)
    new_df["id"] = range(max_id + 1, max_id + 1 + len(new_df))

    # 合并旧数据和新数据
    df = pd.concat([df, new_df], ignore_index=True)

    # 保存到 .csv 文件
    df.to_csv(file_path, index=False)
    
    return df




