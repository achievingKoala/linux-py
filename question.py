grep_commands = [
    {"command": "grep 'keyword' filename", "description": "Search for lines containing 'keyword' in the specified file"},
    {"command": "grep -r 'keyword' directory", "description": "Recursively search for 'keyword' in all files under a directory"},
    {"command": "grep -i 'keyword' filename", "description": "Search for 'keyword' in the specified file, ignoring case"},
    {"command": "grep -n 'keyword' filename", "description": "Show line numbers for lines containing 'keyword'"},
    {"command": "grep -v 'keyword' filename", "description": "Print lines that do not contain 'keyword'"},
    {"command": "grep -l 'keyword' *", "description": "List names of files containing 'keyword'"},
    {"command": "grep -c 'keyword' filename", "description": "Count the occurrences of 'keyword' in the file"},
    {"command": "grep -w 'keyword' filename", "description": "Match only whole words for 'keyword'"},
    {"command": "grep -E 'regex' filename", "description": "Use extended regular expressions for complex matching patterns"},
    {"command": "grep --color 'keyword' filename", "description": "Highlight 'keyword' in output for easier identification"}
]


cut_commands = [
    {"command": "cut -c 1-5 filename.txt", "description": "Extract the first five characters from each line in 'filename.txt'"},
    {"command": "cut -d ',' -f 2 data.csv", "description": "Extract the second field from each line in 'data.csv' using a comma as the delimiter"},
    {"command": "cut -d ' ' -f 1,3,5 report.txt", "description": "Extract the first, third, and fifth fields from each line in 'report.txt'"},
    {"command": "cut -d ':' -f 1 /etc/passwd", "description": "Extract the usernames from the '/etc/passwd' file"}
]
    # {"command": "echo 'apple,banana,cherry' | cut -d ',' -f 2", "description": "Extract the second field from the input string using a pipe"}

cat_commands = [
    {"command": "cat filename.txt", "description": "Display the contents of 'filename.txt'"},
    {"command": "cat file1.txt file2.txt", "description": "Concatenate and display the contents of 'file1.txt' and 'file2.txt'"},
    {"command": "cat -n filename.txt", "description": "Display the contents of 'filename.txt' with line numbers"},
    {"command": "cat -e filename.txt", "description": "Display the contents of 'filename.txt' with a dollar sign at the end of each line"},
    {"command": "cat filename.txt | grep 'keyword'", "description": "Search for 'keyword' in the contents of 'filename.txt' using a pipe"}
]

uniq_commands = [
    {"command": "uniq filename.txt", "description": "Remove adjacent duplicate lines in 'filename.txt'"},
    {"command": "uniq -c filename.txt", "description": "Display unique lines in 'filename.txt' with count of occurrences"},
    {"command": "uniq -d filename.txt", "description": "Display only duplicate lines in 'filename.txt'"},
    {"command": "uniq -u filename.txt", "description": "Display only unique (non-duplicate) lines in 'filename.txt'"},
]

# {"command": "sort -k 2 filename.txt", "description": "Sort 'filename.txt' by the second column"},
# {"command": "sort -t: -k 2 filename.txt", "description": "Sort 'filename.txt' by the second column using ':' as the delimiter"},

sort_commands = [
    {"command": "sort filename.txt", "description": "Sort the contents of 'filename.txt' in ascending order"},
    {"command": "sort -n filename.txt", "description": "Sort 'filename.txt' in ascending numeric order"},
    {"command": "sort -r filename.txt", "description": "Sort 'filename.txt' in descending order"},
    {"command": "sort -u filename.txt", "description": "Sort 'filename.txt' and remove duplicate lines"},
]

# {"command": "tr '[:lower:]' '[:upper:]' < filename.txt", "description": "Convert all lowercase to uppercase using character classes in 'filename.txt'"},

tr_commands = [
    {"command": "tr 'a-z' 'A-Z' < filename.txt", "description": "Convert lowercase letters to uppercase in 'filename.txt'"},
    {"command": "tr -d 'a' < filename.txt", "description": "Delete all occurrences of the letter 'a' in 'filename.txt'"},
    {"command": "tr -s ' ' < filename.txt", "description": "Replace multiple spaces with a single space in 'filename.txt'"},
    {"command": "tr ' ' '\\n' < filename.txt", "description": "Replace spaces with newlines in 'filename.txt'"},
    {"command": "tr -cd '0-9' < filename.txt", "description": "Remove all characters except digits in 'filename.txt'"},
]

shell_commands = [
    {"command": 'str="Hello, Shell"', "description": "Define a string variable 'str' with the value 'Hello, Shell'"},
    {"command": 'num1=5', "description": "Define an integer variable 'num1' with value 5"},
    {"command": 'num2=3', "description": "Define an integer variable 'num2' with value 3"},
    {"command": 'sum=$((num1 + num2))', "description": "Perform integer addition and assign result to 'sum'"},
    {"command": 'arr=("apple" "banana" "cherry")', "description": "Define an array 'arr' with values 'apple', 'banana', 'cherry'"},
    {"command": 'echo ${arr[1]}', "description": "Output the second element of 'arr', which is 'banana'"},

    {"command": 'if [ "$num" -gt 5 ]; then echo "num is greater than 5"; else echo "num is less than or equal to 5"; fi', 
     "description": "Conditionally check if 'num' is greater than 5, output result accordingly"},
    {"command": 'if [ "$str" = "hello" ]; then echo "Strings are equal"; fi', 
     "description": "Check if string 'str' is equal to 'hello', output result if true"},
    {"command": 'if [ -e "file.txt" ]; then echo "File exists"; fi', 
     "description": "Check if 'file.txt' exists in the current directory, output result if true"},

    {"command": 'for item in "${arr[@]}"; do echo "$item"; done', 
     "description": "Loop through each element in 'arr' and print it"},
    {"command": 'for i in {1..5}; do echo "$i"; done', 
     "description": "Loop from 1 to 5 and print each number"},

    {"command": 'count=1', "description": "Initialize variable 'count' to 1"},
    {"command": 'while [ $count -le 5 ]; do echo "Count: $count"; count=$((count + 1)); done', 
     "description": "While loop that increments 'count' from 1 to 5, printing it each time"},

    {"command": 'greet() { echo "Hello, $1!"; }', "description": "Define a function 'greet' that takes one argument and outputs a greeting"},
    {"command": 'greet "Alice"', "description": "Call the function 'greet' with the argument 'Alice'"}
]

shell_dic_commands = [
    {"command": 'declare -A my_dict', "description": "Declare an associative array (dictionary) named 'my_dict'"},
    {"command": 'my_dict["name"]="Alice"', "description": "Set the key 'name' in 'my_dict' with value 'Alice'"},
    {"command": 'my_dict["age"]=30', "description": "Set the key 'age' in 'my_dict' with value 30"},
    {"command": 'echo ${my_dict["name"]}', "description": "Access and print the value associated with the key 'name' in 'my_dict'"},
    {"command": 'for key in "${!my_dict[@]}"; do echo "$key: ${my_dict[$key]}"; done', 
     "description": "Loop through all key-value pairs in 'my_dict' and print each key and its associated value"}
]


user_group_commands = [
    {"command": "sudo useradd username", "description": "Add a new user 'username'"},
    {"command": "sudo userdel username", "description": "Delete the user 'username'"},
    {"command": "sudo usermod -aG groupname username", "description": "Add user 'username' to the group 'groupname'"},
    {"command": "whoami", "description": "Show the currently logged-in username"},
    {"command": "cat /etc/passwd", "description": "View information about all users on the system"},
    {"command": "sudo groupadd groupname", "description": "Add a new group 'groupname'"},
    {"command": "sudo groupdel groupname", "description": "Delete the group 'groupname'"},
    {"command": "sudo groupmod -n newgroupname oldgroupname", "description": "Rename the group from 'oldgroupname' to 'newgroupname'"},
    {"command": "groups username", "description": "Show all groups that user 'username' belongs to"},
    {"command": "cat /etc/group", "description": "View information about all groups on the system"},
    {"command": "ls -l", "description": "Show file and directory permissions"},
    {"command": "chmod 755 filename", "description": "Change the permissions of 'filename' to 755"},
    {"command": "sudo chown username:groupname filename", "description": "Change the owner of 'filename' to 'username' and group to 'groupname'"}
]

process_commands = [
    {"command": "ps aux", "description": "Display all running processes for all users"},
    {"command": "ps -ef | grep firefox", "description": "Filter and display all processes related to Firefox"},
    {"command": "top", "description": "Open a real-time view of system resource usage and processes"},
    {"command": "htop", "description": "Interactive process viewer with a user-friendly interface"},
    {"command": "kill 1234", "description": "Terminate the process with PID 1234"},
    {"command": "kill -9 1234", "description": "Forcefully terminate the process with PID 1234"},
    {"command": "killall firefox", "description": "Terminate all processes named Firefox"},
    {"command": "pkill -u username", "description": "Kill all processes for the specified user"},
    {"command": "./long_running_script.sh &", "description": "Run a script in the background"},
    {"command": "fg %1", "description": "Bring the background job with ID 1 to the foreground"},
    {"command": "jobs", "description": "List all jobs for the current user"},
    {"command": "nice -n 10 ./my_script.sh", "description": "Run 'my_script.sh' with a priority of 10"},
    {"command": "renice -5 -p 1234", "description": "Change the priority of the process with PID 1234 to -5"},
    {"command": "strace -p 1234", "description": "Trace the system calls of the process with PID 1234"}
]

archive_commands = [
    {"command": "tar -czvf archive.tar.gz /path/to/directory", "description": "Create a compressed archive 'archive.tar.gz' from '/path/to/directory'"},
    {"command": "tar -xzvf archive.tar.gz", "description": "Extract 'archive.tar.gz' in the current directory"},
    {"command": "tar -xzvf archive.tar.gz -C /path/to/extract", "description": "Extract 'archive.tar.gz' to '/path/to/extract'"},
    {"command": "gzip filename", "description": "Compress 'filename' to 'filename.gz'"},
    {"command": "gunzip filename.gz", "description": "Decompress 'filename.gz' to its original form"},
    {"command": "gzip -d filename.gz", "description": "Alternative command to decompress 'filename.gz'"},
    {"command": "zip -r archive.zip /path/to/directory", "description": "Create a zip archive 'archive.zip' from '/path/to/directory'"},
    {"command": "unzip archive.zip", "description": "Extract 'archive.zip' in the current directory"},
    {"command": "unzip archive.zip -d /path/to/extract", "description": "Extract 'archive.zip' to '/path/to/extract'"}
]

debian_commands = [
    {"command": "sudo apt update", "description": "Update the list of available packages"},
    {"command": "sudo apt upgrade", "description": "Upgrade all installed packages to the latest versions"},
    {"command": "sudo apt install package_name", "description": "Install a specific package"},
    {"command": "sudo apt remove package_name", "description": "Remove a specific package"},
    {"command": "sudo apt clean", "description": "Clear out the local repository of retrieved package files"},
    {"command": "sudo apt autoremove", "description": "Remove packages that were automatically installed to satisfy dependencies for other packages and are no longer needed"},
    {"command": "sudo dpkg -i package_name.deb", "description": "Install a .deb package file"},
    {"command": "sudo dpkg -r package_name", "description": "Remove an installed package"},
    {"command": "dpkg -l", "description": "List all installed packages"}
]

redhat_commands = [
    {"command": "sudo yum check-update", "description": "Check for available package updates (CentOS 7 and earlier)"},
    {"command": "sudo yum install package_name", "description": "Install a specific package (CentOS 7 and earlier)"},
    {"command": "sudo yum remove package_name", "description": "Remove a specific package (CentOS 7 and earlier)"},
    {"command": "sudo yum update", "description": "Upgrade all installed packages (CentOS 7 and earlier)"},
    {"command": "sudo dnf check-update", "description": "Check for available package updates (CentOS 8 and Fedora)"},
    {"command": "sudo dnf install package_name", "description": "Install a specific package (CentOS 8 and Fedora)"},
    {"command": "sudo dnf remove package_name", "description": "Remove a specific package (CentOS 8 and Fedora)"},
    {"command": "sudo dnf upgrade", "description": "Upgrade all installed packages (CentOS 8 and Fedora)"},
    {"command": "sudo rpm -ivh package_name.rpm", "description": "Install an .rpm package file"},
    {"command": "sudo rpm -e package_name", "description": "Remove an installed package"},
    {"command": "rpm -qi package_name", "description": "Display information about an installed package"}
]

net_high_frequency_commands = [
    {"command": "ping host", "description": "Test the connectivity to a host"},
    {"command": "ssh user@hostname", "description": "Securely log in to a remote host"},
    {"command": "scp file user@host:path", "description": "Securely copy a file to a remote host"},
    {"command": "wget url", "description": "Download a file from a specified URL"},
    {"command": "ip addr show", "description": "Display all network interfaces and their addresses"},
    {"command": "netstat -a", "description": "Show all connections and listening ports"},
    {"command": "netstat -tuln", "description": "Show TCP/UDP listening ports"},
]

net_low_frequency_commands = [
    {"command": "traceroute host", "description": "Trace the route to a host"},
    {"command": "ftp hostname", "description": "Connect to an FTP server"},
    {"command": "sftp user@hostname", "description": "Securely connect to an SFTP server"},
    {"command": "ip route show", "description": "Display the routing table"},
    {"command": "wget -r url", "description": "Recursively download a website"},
    {"command": "ping -c 4 host", "description": "Ping a host 4 times"},
    {"command": "ftp> get file", "description": "Download a file via FTP"},
    {"command": "scp -r directory user@host:path", "description": "Recursively copy a directory to a remote host"},
    {"command": "sftp> put file", "description": "Upload a file via SFTP"}
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

