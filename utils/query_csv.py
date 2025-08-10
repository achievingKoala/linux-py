# import pandas as pd

# def read_docker_data(file_path='csv/command_data.csv'):
#     try:
#         df = pd.read_csv(file_path)
#         return df
#     except FileNotFoundError:
#         print(f"Error: The file {file_path} does not exist.")
#         return None
#     except pd.errors.EmptyDataError:
#         print("Error: The file is empty.")
#         return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

# def get_commands(command_group='docker_swarm_commands'):
#     df = read_docker_data()
#     if df is not None:
#         return df[df['command_group'] == command_group].to_dict(orient='records')
#     return []

import random
import pandas as pd
import sqlite3

def load_csv_to_sqlite(file_path, table_name, conn):
    try:
        df = pd.read_csv(file_path, dtype = {'command_id': "Int64"})
        
        # Ensure the 'id' and 'command_id' columns are integers
        if 'id' in df.columns:
            df['id'] = pd.to_numeric(df['id'], errors='coerce').fillna(0).astype(int)
        if 'command_id' in df.columns:
            df['command_id'] = pd.to_numeric(df['command_id'], errors='coerce').fillna(0).astype(int)
        
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        return True
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return False
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def query_random_data(key_words=['docker','k8s'], limit=5):
    with sqlite3.connect(':memory:') as conn:
        # Load both CSV files into SQLite tables
        if not load_csv_to_sqlite('csv/command_data.csv', 'command_data', conn):
            return []
        
        query = """
        select distinct command_group from command_data
        """
        # Construct the WHERE clause for fuzzy matching
        # where_clause = ' OR '.join("command_data.command_group LIKE ?" for _ in command_group_key_word)
        # Construct the WHERE clause for fuzzy matching excluding 'docker' and 'k8s' command groups
        # where_clause = ' AND '.join("command_data.command_group NOT LIKE ?" for _ in key_words)
        # query = query.format(where_clause)
        # fuzzy_keywords = [f"%{kw}%" for kw in key_words]
        # Prepare keywords for fuzzy matching
        result = pd.read_sql_query(query, conn, params= ())

        array = [x['command_group']  for x in result.to_dict(orient='records')]
        array = [x for x in array if not any(kw in x for kw in key_words)]
        return random.sample(array, 2)


# print(query_random_data())

def query_exclude_data(key_words=['docker','k8s'], limit=5):
    with sqlite3.connect(':memory:') as conn:
        # Load both CSV files into SQLite tables
        if not load_csv_to_sqlite('csv/command_data.csv', 'command_data', conn):
            return []
        if not load_csv_to_sqlite('csv/count.csv', 'count', conn):
            return []
        query = """
        SELECT command_data.id, command_data.command, command_data.description, count.command_id, count(count.command_id) as pCount
        , SUM(CASE WHEN count.is_correct = 1 THEN 1 ELSE 0 END) as tCount
        FROM command_data 
        LEFT JOIN count ON command_data.id = count.command_id
        WHERE {}
        GROUP BY command_data.id
        ORDER BY pCount, tCount
        LIMIT ?
        """
        # Construct the WHERE clause for fuzzy matching
        # where_clause = ' OR '.join("command_data.command_group LIKE ?" for _ in command_group_key_word)
        # Construct the WHERE clause for fuzzy matching excluding 'docker' and 'k8s' command groups
        where_clause = ' AND '.join("command_data.command_group NOT LIKE ?" for _ in key_words)
        query = query.format(where_clause)
        # Prepare keywords for fuzzy matching
        fuzzy_keywords = [f"%{kw}%" for kw in key_words]
        result = pd.read_sql_query(query, conn, params= fuzzy_keywords + [limit])

        return result.to_dict(orient='records')
    
def query_fuzzy_data(command_group_key_word=['docker'], limit=5):
    with sqlite3.connect(':memory:') as conn:
        # Load both CSV files into SQLite tables
        if not load_csv_to_sqlite('csv/command_data.csv', 'command_data', conn):
            return []
        if not load_csv_to_sqlite('csv/count.csv', 'count', conn):
            return []
        query = """
        SELECT command_data.id, command_data.command, command_data.description, count.command_id, count(count.command_id) as pCount
        , SUM(CASE WHEN count.is_correct = 1 THEN 1 ELSE 0 END) as tCount
        FROM command_data 
        LEFT JOIN count ON command_data.id = count.command_id
        WHERE {}
        GROUP BY command_data.id
        ORDER BY pCount, tCount
        LIMIT ?
        """
        # Construct the WHERE clause for fuzzy matching
        where_clause = ' OR '.join("command_data.command_group LIKE ?" for _ in command_group_key_word)
        
        query = query.format(where_clause)
        # Prepare keywords for fuzzy matching
        fuzzy_keywords = [f"%{kw}%" for kw in command_group_key_word]
        result = pd.read_sql_query(query, conn, params=fuzzy_keywords + [limit])

        return result.to_dict(orient='records')

def query_joined_data(command_group=['process_commands'], limit=5):
    with sqlite3.connect(':memory:') as conn:
        # Load both CSV files into SQLite tables
        if not load_csv_to_sqlite('csv/command_data.csv', 'command_data', conn):
            return []
        if not load_csv_to_sqlite('csv/count.csv', 'count', conn):
            return []
        
        # Execute SQL JOIN query
        query = """
        SELECT 
        command_data.id, 
        command_data.ignore, command_data.command, command_data.description, count.command_id, count(count.command_id) as pCount
        , SUM(CASE WHEN count.is_correct = 1 THEN 1 ELSE 0 END) as tCount
        FROM command_data 
        LEFT JOIN count ON command_data.id = count.command_id
        WHERE command_data.command_group IN ({})
        and command_data.ignore is NULL
        GROUP BY command_data.id
        ORDER BY pCount, tCount
        LIMIT ?
        """
        placeholders = ','.join('?' for _ in command_group)
        query = query.format(placeholders)
        result = pd.read_sql_query(query, conn, params=command_group + [limit])

        return result.to_dict(orient='records')

def query_min_data(exclude_words= ['k8s', 'docker', 'cron_more', 'package'], command_group=['process_commands'], limit=100):
    with sqlite3.connect(':memory:') as conn:
        # Load both CSV files into SQLite tables
        if not load_csv_to_sqlite('csv/command_data.csv', 'command_data', conn):
            return []
        if not load_csv_to_sqlite('csv/count.csv', 'count', conn):
            return []
        
        # Execute SQL JOIN query
        query = """
        SELECT 
        command_data.id, 
        command_data.command, 
        command_data.command_group, 
        command_data.description, 
        count.command_id, 
        count(count.command_id) as pCount, 
        SUM(CASE WHEN count.is_correct = 1 THEN 1 ELSE 0 END) as tCount
        FROM command_data 
        LEFT JOIN count ON command_data.id = count.command_id
        where {}
        GROUP BY command_data.id
        ORDER BY pCount, tCount
        LIMIT ?
        """
        placeholders = ' and '.join("command_data.command_group NOT LIKE ?" for _ in exclude_words)         
        query = query.format(placeholders)
        # [f'%{word}%'for word in exclude_words]
        fuzzy_keywords = [f"%{kw}%" for kw in exclude_words]
        result = pd.read_sql_query(query, conn, params= fuzzy_keywords + [limit])
        # result = pd.read_sql_query(query, conn, params=[limit])

        # return result.to_dict(orient='records')
        # return [ x['command_group'] for x in result.to_dict(orient='records')]
        # Count the occurrences of each command_group and return the top 5
        command_groups = [x['command_group'] for x in result.to_dict(orient='records')]
        top_5_command_groups = pd.Series(command_groups).value_counts().head(5).index.tolist()

        return top_5_command_groups

def query_min_group_data(exclude_words= ['k8s', 'docker', 'cron_more', 'package'], command_group=['process_commands'], limit=100):
    with sqlite3.connect(':memory:') as conn:
        # Load both CSV files into SQLite tables
        if not load_csv_to_sqlite('csv/command_data.csv', 'command_data', conn):
            return []
        if not load_csv_to_sqlite('csv/count.csv', 'count', conn):
            return []
        
        # Execute SQL JOIN query
        # query = """
        # SELECT 
        # command_data.id, 
        # command_data.command, 
        # command_data.command_group, 
        # command_data.description, 
        # count.command_id, 
        # count(count.command_id) as pCount,
        # SUM(CASE WHEN count.is_correct = 1 THEN 1 ELSE 0 END) as tCount,
        # count(command_data.command) as questC,
        # (count(count.command_id) + 0.0) / count(command_data.id) as average
        # FROM command_data 
        # LEFT JOIN count ON command_data.id = count.command_id
        # where {}
        # GROUP BY command_data.command_group
        # ORDER BY average, pCount
        # LIMIT ?
        # """
        # Execute SQL JOIN query
        query = """
        SELECT 
        command_data.id,
        command_data.command_group, 
        command_data.description, 
        count(count.id) as tryC, 
        count(distinct command_data.id) as questC,
        Round((count(count.id) + 0.0) / count(distinct command_data.id), 2) as averageC
        FROM command_data
        left join count
        on command_data.id = count.command_id
        where {}
        GROUP BY command_data.command_group
        ORDER BY averageC, tryC
        LIMIT ?
        """
        placeholders = ' and '.join("command_data.command_group NOT LIKE ?" for _ in exclude_words)         
        query = query.format(placeholders)
        # [f'%{word}%'for word in exclude_words]
        fuzzy_keywords = [f"%{kw}%" for kw in exclude_words]
        result = pd.read_sql_query(query, conn, params= fuzzy_keywords + [limit])
        # result = pd.read_sql_query(query, conn, params=[limit])
        return [ x['command_group'] for x in result.to_dict(orient='records')][0:5]

# result = query_min_group_data()
# print()
# for line in result:
    # print(f"{line['command_group']} {line['pCount']} {line['average']} {line['questC']}")
    # print(line)
# print(len(result))

def merge_and_load_to_sql():
    try:
        # Read both CSV files
        command_data = pd.read_csv('csv/command_data.csv')
        count_data = pd.read_csv('csv/count.csv')
        
        # Merge the dataframes on id and command_id
        merged_df = pd.merge(
            command_data, 
            count_data,
            left_on='id',
            right_on='command_id',
            how='left'
        )
        
        # Connect to SQLite database
        with sqlite3.connect('commands.db') as conn:
            # Save merged data to SQL table
            merged_df.to_sql('merged_commands', conn, if_exists='replace', index=False)
            print("Successfully merged data and loaded to SQL database")
            
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the merge and load
# merge_and_load_to_sql()

# df = pd.read_csv('csv/command_data.csv')
# print(f"Type of command_id column: {df['id'].dtype}")

def query_merged_commands():
    try:
        # Connect to the SQLite database
        with sqlite3.connect('commands.db') as conn:
            # Define your SQL query
            query = "SELECT * FROM merged_commands"
            
            # Execute the query and load the result into a DataFrame
            result_df = pd.read_sql_query(query, conn)
            
            # Convert the result to a dictionary or print it
            return result_df.to_dict(orient='records')
    except Exception as e:
        print(f"An error occurred while querying the database: {e}")
        return []

# Example usage
# result = query_merged_commands()
# for line in result:
#     print(line)










