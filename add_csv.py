import csv

def update_count_csv(command_id, command, correct, file_path='csv/count.csv'):
    new_row = [command_id, command, correct]
    try:
        # 读取现有数据
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        # 在第一行后插入新行
        data.insert(1, new_row)
        
        # 写回文件
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        
        print("Row added successfully after the first line.")
    except Exception as e:
        print(f"An error occurred while updating the CSV: {e}")

# Example usage
update_count_csv(33, 'docker run -d --name container_name image_name[:tag]', 'True')

