import pandas as pd

def read_docker_data(file_path='csv/dockerData.csv'):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_commands(command_group='docker_swarm_commands'):
    df = read_docker_data()
    if df is not None:
        return df[df['command_group'] == command_group].to_dict(orient='records')
    return []

print(get_commands())





