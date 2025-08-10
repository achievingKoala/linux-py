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
    

    {"command": "docker logs container_name", "description": "Fetch the logs of a container"},
    {"command": "docker logs -f container_name", "description": "Follow logs of a container in real-time"},
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
    {"command": "build: context: ./backend, dockerfile: Dockerfile", "description": "Specify build options for the service, including context and Dockerfile"},
    {"command": "image: nginx:latest", "description": "Specify the Docker image to use for the service"},
    {"command": "ports: '80:80', '5000:5000'", "description": "Map ports from the host to the container"},
    {"command": "volumes: './data:/data', 'db_data:/var/lib/mysql'", "description": "Mount host directories or volumes to the container"},
    {"command": "environment: MYSQL_ROOT_PASSWORD: example", "description": "Set environment variables for the service"},
    {"command": "depends_on: backend", "description": "Specify dependencies between services, ensuring one starts before another"},
    {"command": "networks: my_network", "description": "Define custom networks for communication between services"},
    {"command": "command: [\"python3\", \"app.py\"]", "description": "Override the default command for the service"},
    {"command": "docker compose up -d --build", "description": "Start services in detached mode (background)"},
    {"command": "docker compose down --volumes", "description": "Stop and remove all services and networks defined in the Compose file"},
    {"command": "docker compose ps", "description": "List the status of the services defined in the Compose file"},
    {"command": "docker compose logs --follow", "description": "View the logs for services defined in the Compose file"},
    {"command": "docker compose restart service_name", "description": "Restart the services defined in the Compose file"},
]

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

docker_nginx_swarm_commands = [
    {"command": "docker swarm init", "description": "Initialize a new Docker Swarm"},
    {"command": "docker service create --name nginx_cluster --replicas 3 -p 80:80 nginx", "description": "Create an Nginx service with 3 replicas, exposing port 80"},
    {"command": "docker service ls", "description": "List all services to verify the deployment"},
    {"command": "docker service ps nginx_cluster", "description": "Check the status and replica count of the Nginx service"},
    {"command": "docker service scale nginx_cluster=5", "description": "Scale the Nginx service to 5 replicas"},
    {"command": "docker service update --image nginx:latest nginx_cluster", "description": "Update the Nginx service to use the latest image"},
    {"command": "docker service rm nginx_cluster", "description": "Remove the Nginx service from the Swarm"},
]


# {"command": "docker system prune -a", "description": "Clean up unused images, containers, and volumes"}