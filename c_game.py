import random
from question import grep_commands, cut_commands, cat_commands, sort_commands, uniq_commands, tr_commands, shell_commands, shell_dic_commands, user_group_commands
from question import process_commands, archive_commands, high_frequency_commands, low_frequency_commands, redhat_commands, debian_commands
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


awk_commands = [
    {"command": "awk '{print $1}'", "description": 'Print the first field of each input line'},
    {"command": "awk -F, '{print $2}' file.csv", "description": 'Print the second field of a CSV file'},
    {"command": "awk '/pattern/ {print}'", "description": 'Print lines matching a specified pattern'},
    {"command": "awk '{sum += $1} END {print sum}'", "description": 'Sum the first field of all input lines'},
    {"command": "awk '{if ($1 > 10) print}'", "description": 'Print lines where the first field is greater than 10'},
    {"command": "awk '{print NR, $0}'", "description": 'Print line number followed by the entire line'},
    {"command": "awk -F: '{print $1}' /etc/passwd", "description": 'Print the usernames from the /etc/passwd file'},
]

# "sed": "Stream editor for filtering and transforming text",
# {"command": "sed -e 's/(.*)/\\U\\1/'", "description": "Convert the entire line to uppercase"},
sed_commands = [
    {"command": "sed 's/old/new/g' file.txt", "description": "Replace all occurrences of 'old' with 'new' in file.txt"},
    {"command": "sed -n '3p' file.txt", "description": "Print the third line of file.txt"},
    {"command": "sed '1d' file.txt", "description": "Delete the first line of file.txt"},
    {"command": "sed -e 's/foo/bar/' -e 's/baz/qux/'", "description": "Replace 'foo' with 'bar' and 'baz' with 'qux'"},
    {"command": "sed -i 's/old/new/g' file.txt", "description": "Edit file.txt in place, replacing 'old' with 'new'"},
    {"command": "sed -n '/pattern/p' file.txt", "description": "Print lines that match a specified pattern"},
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
    # {"command": "find /dir -exec rm {} \\;", "description": "Find files and execute a command on each (e.g., delete matching files)"},
]

docker_basic_commands = [
    {"command": "docker search image_name", "description": "Search for an image in Docker Hub"},
    {"command": "docker pull mysql:tag", "description": "Download the MySQL image with a specific tag from Docker Hub"},
    {"command": "docker images", "description": "List all local images"},
    {"command": "docker rmi image_id_or_name", "description": "Remove an image by ID or name"},
    
    {"command": "docker run -d --name container_name image_name[:tag]", "description": "Create and start a container in detached mode"},
    {"command": "docker ps", "description": "List all running containers"},
    {"command": "docker ps -a", "description": "List all containers, including stopped ones"},
    {"command": "docker start container_id_or_name", "description": "Start a stopped container"},
    {"command": "docker stop container_id_or_name", "description": "Stop a running container"},
    {"command": "docker restart container_id_or_name", "description": "Restart a container"},
    {"command": "docker rm container_id_or_name", "description": "Remove a container by ID or name"},
    {"command": "docker exec -it container_id_or_name /bin/bash", "description": "Access a running container with an interactive terminal"},
]

docker_advance_commands = [    
    {"command": "docker network ls", "description": "List all Docker networks"},
    {"command": "docker network create network_name", "description": "Create a new Docker network"},
    {"command": "docker network connect network_name container_id_or_name", "description": "Connect a container to a network"},
    {"command": "docker network disconnect network_name container_id_or_name", "description": "Disconnect a container from a network"},
    
    {"command": "docker volume create volume_name", "description": "Create a new Docker volume"},
    {"command": "docker volume ls", "description": "List all Docker volumes"},
    {"command": "docker run -d -v volume_name:/container_path image_name", "description": "Mount a volume to a container"},
    {"command": "docker volume rm volume_name", "description": "Remove a Docker volume by name"},
    
    {"command": "docker system prune -a", "description": "Clean up unused images, containers, and volumes"}
]


dockerfile_commands = [
    {"command": "FROM ubuntu:20.04", "description": "Specify the base image for the Dockerfile"},
    {"command": "WORKDIR /app", "description": "Set the working directory for commands in the Dockerfile"},
    {"command": "COPY . /app", "description": "Copy files from the host to the container"},
    {"command": "RUN apt-get update && apt-get install -y python3", "description": "Execute commands to install dependencies"},
    {"command": "EXPOSE 80", "description": "Expose a port to allow external access to the container"},
    {"command": "CMD [\"python3\", \"app.py\"]", "description": "Set the default command to run when the container starts"},
    {"command": "VOLUME /data", "description": "Define a volume for shared data between host and container"},
]

dockerfile_more_comands = [
    {"command": "LABEL version=\"1.0\"", "description": "Add metadata to the image"},
    {"command": "ADD package.tar.gz /app", "description": "Copy and extract a tar file from the host to the container"},
    {"command": "ENTRYPOINT [\"python3\", \"app.py\"]", "description": "Define the main executable when the container starts"},
    {"command": "ENV APP_ENV production", "description": "Set environment variables"},
    {"command": "USER appuser", "description": "Specify the user to run the container with"},
    {"command": "ARG VERSION=1.0", "description": "Define a build-time variable"},
    {"command": "HEALTHCHECK CMD curl --fail http://localhost || exit 1", "description": "Set a health check command to verify container status"}
]

docker_compose_commands = [
    {"command": "version: '3.8'", "description": "Specify the version of the Docker Compose file format"},
    {"command": "services:", "description": "Define the services that make up the application"},
    {"command": "build:", "description": "Specify build options for the service, including context and Dockerfile", "parameters": "context: ./backend, dockerfile: Dockerfile"},
    {"command": "image:", "description": "Specify the Docker image to use for the service", "parameters": "nginx:latest"},
    {"command": "ports:", "description": "Map ports from the host to the container", "parameters": "'80:80', '5000:5000'"},
    {"command": "volumes:", "description": "Mount host directories or volumes to the container", "parameters": "'./data:/data', 'db_data:/var/lib/mysql'"},
    {"command": "environment:", "description": "Set environment variables for the service", "parameters": "MYSQL_ROOT_PASSWORD: example"},
    {"command": "depends_on:", "description": "Specify dependencies between services, ensuring one starts before another", "parameters": "backend"},
    {"command": "networks:", "description": "Define custom networks for communication between services", "parameters": "my_network"},
    {"command": "command:", "description": "Override the default command for the service", "parameters": "[\"python3\", \"app.py\"]"},
    {"command": "docker compose up -d", "description": "Start services in detached mode (background)", "parameters": "--build"},
    {"command": "docker compose down", "description": "Stop and remove all services and networks defined in the Compose file", "parameters": "--volumes"},
    {"command": "docker compose ps", "description": "List the status of the services defined in the Compose file", "parameters": ""},
    {"command": "docker compose logs", "description": "View the logs for services defined in the Compose file", "parameters": "--follow"},
    {"command": "docker compose restart", "description": "Restart the services defined in the Compose file", "parameters": "service_name"},
]

commands = docker_compose_commands
# + uniq_commands

def quiz_user():
    score = 0
    total_questions =  5 if (len(commands) >= 5) else len(commands)

    questions = random.sample(commands, total_questions)  # Get unique questions

    for question in questions:  # Iterate over unique questions
        print(f"Command description: '{question['description']}'")
        
        user_answer = input("What is the command? ")
        
        if user_answer.lower() == question['command'].lower():
            print("\033[92mCorrect!\033[0m\n")
            score += 1
        else:
            print(f"\033[94mThe correct answer is : {question['command']}\033[0m\n")

    print(f"Your final score: {score}/{total_questions}")

if __name__ == "__main__":
    print("Welcome to the Linux Commands Quiz Game!")
    quiz_user()
