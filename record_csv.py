import csv

def update_count_csv(command_id, command, correct, file_path='csv/count.csv'):
    # new_row = [command_id, command, correct]
    try:
        # 读取现有数据
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        # 获取最大 command_id 并自增
        if len(data) > 1:
            last_id = max(int(row[0]) for row in data[1:] if row[0].isdigit())
        else:
            last_id = 0
        new_id = last_id + 1
        
        new_row = [new_id, command_id, command, correct]
        
        # 在第一行后插入新行
        data.append(new_row)
        
        # 写回文件
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        
        print("Row added successfully after the first line.")
    except Exception as e:
        print(f"An error occurred while updating the CSV: {e}")

# Example usage
update_count_csv(56, 'docker run -d --name container_name image_name[:tag]', 'True')

