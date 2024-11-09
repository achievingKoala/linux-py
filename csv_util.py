import pandas as pd
import os
from question import docker_swarm_commands, docker_nginx_swarm_commands
from c_game import dockerfile_commands, docker_compose_commands, dockerfile_more_comands

docker_swarm_commands = [
    {"command": "docker swarm init", "description": "Initialize a new Docker Swarm"},
    {"command": "docker swarm join --token token manager-ip:port", "description": "Join a node to the Swarm using the provided token"},
    {"command": "docker node ls", "description": "List all nodes in the Swarm"},
    {"command": "docker node rm node-id", "description": "Remove a node from the Swarm by node ID"},
    {"command": "docker service create --name service-name --replicas number image", "description": "Create a new service in the Swarm with specified replicas"},
    {"command": "docker service ls", "description": "List all services in the Swarm"},
    {"command": "docker service scale service-name=replicas", "description": "Scale a service to the specified number of replicas"},
    {"command": "docker service update --image new-image service-name", "description": "Update a service to use a new image"},
    {"command": "docker service rm service-name", "description": "Remove a service from the Swarm"},
    {"command": "docker stack deploy -c compose-file stack-name", "description": "Deploy a stack using a Docker Compose file"},
    {"command": "docker stack rm stack-name", "description": "Remove a stack from the Swarm"},
    {"command": "docker stack ls", "description": "List all stacks in the Swarm"},
    {"command": "docker stack services stack-name", "description": "List all services in a specific stack"},
    {"command": "docker node update --availability drain/pause/active node-id", "description": "Update the availability status of a node"},
]

def save_commands_to_csv(commands_array, array_name, file_path='csv/dockerData.csv'):
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

# Example usage with docker_swarm_commands
save_commands_to_csv(dockerfile_more_comands, 'dockerfile_more_comands')



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



