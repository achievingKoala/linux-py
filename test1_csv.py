from scripts.question import process_commands, archive_commands

import csv

cut_commands = [
    {"command": "cut -c 1-5 filename.txt", "description": "Extract the first five characters from each line in 'filename.txt'"},
    {"command": "cut -d ',' -f 2 data.csv", "description": "Extract the second field from each line in 'data.csv' using a comma as the delimiter"},
    {"command": "cut -d ' ' -f 1,3,5 report.txt", "description": "Extract the first, third, and fifth fields from each line in 'report.txt'"},
    {"command": "cut -d ':' -f 1 /etc/passwd", "description": "Extract the usernames from the '/etc/passwd' file"}
]
def save_cut_commands_to_csv(commands_row):
    with open('csv/commands.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Command', 'Description'])
        for command in cut_commands:
            writer.writerow([command['command'], command['description']])

save_cut_commands_to_csv('a')

# Define the data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]


# # Create a CSV file and write the data
# with open('csv/output1.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


