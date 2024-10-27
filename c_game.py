import random

# Linux commands and their descriptions
commands = {
    'ls': 'List directory contents',
    'cd': 'Change the current directory',
    'pwd': 'Print working directory',
    'mkdir': 'Make directories',
    'rmdir': 'Remove empty directories',
    'rm': 'Remove files or directories',
    'touch': 'Change file timestamps or create an empty file',
    'cp': 'Copy files and directories',
    'mv': 'Move (rename) files',
    'cat': 'Concatenate files and print on the standard output',
}

docker_commands = {
    'docker pull': 'Pull an image from a registry',
    'docker run': 'Run a command in a new container',
    'docker ps': 'List running containers',
    'docker build': 'Build an image from a Dockerfile',
    'docker stop': 'Stop a running container',
    'docker rm': 'Remove one or more containers',
    'docker rmi': 'Remove one or more images',
    'docker exec': 'Run a command in a running container',
    'docker logs': 'Fetch the logs of a container',
    'docker images': 'List images on the host',
    'docker network ls': 'List all networks',
    'docker volume ls': 'List all volumes',
    'docker-compose up': 'Start services defined in a docker-compose.yml file',
    'docker-compose down': 'Stop and remove services, networks, and volumes defined in docker-compose.yml',
}


awk_commands = {
    "awk '{print $1}'": 'Print the first field of each input line',
    "awk -F, '{print $2}' file.csv": 'Print the second field of a CSV file',
    "awk '/pattern/ {print}'": 'Print lines matching a specified pattern',
    "awk '{sum += $1} END {print sum}'": 'Sum the first field of all input lines',
    "awk '{if ($1 > 10) print}'": 'Print lines where the first field is greater than 10',
    "awk '{print NR, $0}'": 'Print line number followed by the entire line',
    "awk -F: '{print $1}' /etc/passwd": 'Print the usernames from the /etc/passwd file',
}

# "sed": "Stream editor for filtering and transforming text",
sed_commands = [
    {"command": "sed 's/old/new/g' file.txt", "description": "Replace all occurrences of 'old' with 'new' in file.txt"},
    {"command": "sed -n '3p' file.txt", "description": "Print the third line of file.txt"},
    {"command": "sed '1d' file.txt", "description": "Delete the first line of file.txt"},
    {"command": "sed -e 's/foo/bar/' -e 's/baz/qux/'", "description": "Replace 'foo' with 'bar' and 'baz' with 'qux'"},
    {"command": "sed -i 's/old/new/g' file.txt", "description": "Edit file.txt in place, replacing 'old' with 'new'"},
    {"command": "sed -n '/pattern/p' file.txt", "description": "Print lines that match a specified pattern"},
    {"command": "sed -e 's/(.*)/\\U\\1/'", "description": "Convert the entire line to uppercase"},
]

find_commands = [
    {"command": "find /dir -name 'filename'", "description": "Find a file with a specific name in a dir"},
    {"command": "find /dir -type f", "description": "Find all regular files in a dir"},
    {"command": "find /dir -type d", "description": "Find all directories in a dir"},
    {"command": "find /dir -size +50M", "description": "Find files larger than 50MB in a dir"},
    {"command": "find /dir -size -10k", "description": "Find files smaller than 10KB in a dir"},
    {"command": "find /dir -mtime -7", "description": "Find files modified within the last 7 days"},
    {"command": "find /dir -atime +30", "description": "Find files accessed more than 30 days ago"},
    {"command": "find /dir -perm 644", "description": "Find files with permissions set to 644"},
    {"command": "find /dir -user username", "description": "Find files owned by a specific user"},
    {"command": "find /dir -group groupname", "description": "Find files owned by a specific group"},
    {"command": "find /dir -maxdepth 2 -name '*.conf'", "description": "Find .conf files in a dir, limiting search to a depth of 2"},
    {"command": "find /dir -exec rm {} \\;", "description": "Find files and execute a command on each (e.g., delete matching files)"},
]

commands = find_commands

def quiz_user():
    score = 0
    total_questions = 5

    questions = random.sample(commands, total_questions)  # Get unique questions

    for question in questions:  # Iterate over unique questions
        print(f"Command description: '{question['description']}'")
        
        user_answer = input("What is the command? ")
        
        if user_answer.lower() == question['command'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['command']}\n")

    print(f"Your final score: {score}/{total_questions}")

if __name__ == "__main__":
    print("Welcome to the Linux Commands Quiz Game!")
    quiz_user()
