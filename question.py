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
    {"command": "cut -d ':' -f 1 /etc/passwd", "description": "Extract the usernames from the '/etc/passwd' file"},
    # {"command": "echo 'apple,banana,cherry' | cut -d ',' -f 2", "description": "Extract the second field from the input string using a pipe"}
]

cat_commands = [
    {"command": "cat filename.txt", "description": "Display the contents of 'filename.txt'"},
    {"command": "cat file1.txt file2.txt", "description": "Concatenate and display the contents of 'file1.txt' and 'file2.txt'"},
    {"command": "cat -n filename.txt", "description": "Display the contents of 'filename.txt' with line numbers"},
    {"command": "cat -e filename.txt", "description": "Display the contents of 'filename.txt' with a dollar sign at the end of each line"},
    {"command": "cat filename.txt | grep 'keyword'", "description": "Search for 'keyword' in the contents of 'filename.txt' using a pipe"}
]

