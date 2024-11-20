view_logs_commands = [
    {"command": "cat /var/log/syslog", "description": "View the entire content of the syslog file"},
    {"command": "less /var/log/syslog", "description": "View the syslog file with pagination"},
    {"command": "more /var/log/syslog", "description": "View the syslog file with pagination (alternative to less)"},
    {"command": "tail /var/log/syslog", "description": "View the last few lines of the syslog file"},
    {"command": "tail -f /var/log/syslog", "description": "Monitor and view new log entries in real-time"},
    {"command": "head /var/log/syslog", "description": "View the first few lines of the syslog file"},
]

search_logs_commands = [
    {"command": "grep 'error' /var/log/syslog", "description": "Search for the term 'error' in the syslog file"},
    {"command": "grep -i 'error' /var/log/syslog", "description": "Search for 'error' in the syslog file, ignoring case"},
    {"command": "grep -r 'error' /var/log/", "description": "Search for 'error' recursively in all files under /var/log/"},
    {"command": "grep -A 3 'error' /var/log/syslog", "description": "Display matching lines and the 3 lines after them"},
    {"command": "grep -B 3 'error' /var/log/syslog", "description": "Display matching lines and the 3 lines before them"},
    {"command": "grep -C 3 'error' /var/log/syslog", "description": "Display matching lines and 3 lines before and after them"},
]

# {"command": "journalctl", "description": "View all system logs managed by systemd"},
journalctl_commands = [
    {"command": "journalctl -n 50", "description": "View the last 50 lines of logs from journal"},
    {"command": "journalctl -u nginx", "description": "View logs for the nginx service"},
    {"command": "journalctl --since '2024-11-01'", "description": "View logs since November 1, 2024"},
    {"command": "journalctl --until '2024-11-10'", "description": "View logs until November 10, 2024"},
    {"command": "journalctl -f", "description": "View and follow logs in real-time, similar to 'tail -f'"},
    {"command": "journalctl -b", "description": "View logs for the current boot session"},
]

# {"command": "egrep '^[AEIOUaeiou]' filename", "description": "Find lines starting with a vowel in the specified file"},
# {"command": "egrep -i 'error|fail' filename", "description": "Find lines containing 'error' or 'fail', case insensitive"},
# {"command": "egrep -v '^#' filename", "description": "Find lines that do not start with a '#' character (useful for configuration files)"},
# {"command": "egrep '[^\x00-\x7F]' filename", "description": "Find lines containing non-ASCII characters"},

egrep_commands = [
    {"command": "egrep '[0-9]+' filename", "description": "Find lines containing one or more digits in the specified file"},
    {"command": "egrep '^.{10}$' filename", "description": "Find lines that are exactly ten characters long"},    
    {"command": "egrep 'foo|bar' filename", "description": "Find lines containing either 'foo' or 'bar'"},
    {"command": "egrep '\s' filename", "description": "Find lines containing whitespace characters in the specified file"},
    {"command": "egrep 'https?://' filename", "description": "Find lines containing URLs that start with http or https"},
    {"command": "egrep '([A-Za-z]+\s){3,}' filename", "description": "Find lines containing three or more words"},
    {"command": "egrep '.+\\.log$' /dir", "description": "Find files that have a .log extension"},
    {"command": "egrep -l 'pattern' /dir/*", "description": "Find files containing 'pattern' and list their file names"},
    {"command": "egrep -rl 'pattern' /dir", "description": "Recursively find files containing 'pattern' and list their file names in the specified directory"},
]
egrep_commands.append(
    {"command": "egrep -l filename /dir/*", "description": "Use egrep to locate a file named 'filename' and list its file names in the specified directory"}
)






logrotate_commands = [
    {"command": "sudo logrotate /etc/logrotate.conf", "description": "Manually run logrotate using the global configuration"},
    {"command": "sudo cat /etc/logrotate.d/your_log_config", "description": "View the logrotate configuration for a specific log file"},
]

file_size_commands = [
    {"command": "du -sh /var/log/", "description": "View the disk usage of the /var/log directory"},
    {"command": "ls -lh /var/log/syslog", "description": "View detailed information (size, permissions, etc.) for the syslog file"},
]

clear_logs_commands = [
    {"command": "sudo rm /var/log/old_log_file", "description": "Manually delete a specific old log file"},
]

kernel_log_commands = [
    {"command": "dmesg", "description": "View kernel log messages, typically for hardware and system startup information"},
    {"command": "dmesg | grep 'error'", "description": "Search for 'error' in the kernel log messages"},
]

auditd_commands = [
    {"command": "ausearch -m avc", "description": "Search for 'AVC' messages in audit logs"},
    {"command": "auditctl -w /etc/passwd -p wa", "description": "Set audit rule to watch changes to /etc/passwd with write and attribute changes"},
]

file_permission_commands = [
    {"command": "sudo chmod 644 /var/log/syslog", "description": "Change permissions of the syslog file (readable by all, writable by owner)"},
    {"command": "sudo chown root:adm /var/log/syslog", "description": "Change the owner and group of the syslog file to root:adm"},
]
