cron_commands = [
    {"command": "crontab -l", "description": "List the current user's cron jobs"},
    {"command": "crontab -r", "description": "Remove the current user's cron jobs"},
    {"command": "crontab -e", "description": "Add or edit cron job for the current user"},
    {"command": "crontab -u username -l", "description": "List all cron jobs for a specific user 'username'"},
    {"command": "for user in $(cut -f1 -d: /etc/passwd); do echo $user; crontab -u $user -l; done", "description": "See all users' cron jobs"},
    {"command": "* * * * * /path/to/script.sh", "description": "Cron job to execute a .sh file every minute"},
    {"command": "minute", "description": "the 1st '*'"},
    {"command": "hour", "description": "the 2nd '*'"},
    {"command": "day_of_month", "description": "the 3rd '*'"},
    {"command": "month", "description": "the 4th '*'"},
    {"command": "day_of_week", "description": "the 5th '*'"},
]


cron_more_commands = [
    {"command": "0 0 * * * /path/to/daily_backup.sh", "description": "Cron job to run a daily backup at midnight"},
    {"command": "0 9 * * 1-5 /path/to/weekday_script.sh", "description": "Cron job to execute a script every weekday at 9 AM"},
    {"command": "30 18 * * 1-5 /path/to/weekday_evening_task.sh", "description": "Cron job to run a task at 6:30 PM on weekdays"},
    {"command": "0 12 1 * * /path/to/monthly_report.sh", "description": "Cron job to generate a report on the 1st day of every month at noon"},
    {"command": "15 2 * * * /path/to/morning_task.sh", "description": "Cron job to run a task at 2:15 AM every day"},
]

# # Splitting the "*" explanation into separate commands:
# {"command": "* * * * * /path/to/script.sh", "description": "Cron job to execute a .sh file every minute"},
# {"command": "* * * * *", "description": "Every hour (the second '*') represents 'hour'"},
# {"command": "* * * * *", "description": "Every day (the third '*') represents 'day of the month'"},
# {"command": "* * * * *", "description": "Every month (the fourth '*') represents 'month'"},
# {"command": "* * * * *", "description": "Every day of the week (the fifth '*') represents 'day of the week'"}

# {"command": "systemctl status cron", "description": "Check if the cron service is running"},
# {"command": "systemctl start cron", "description": "Start the cron service"},
# {"command": "systemctl stop cron", "description": "Stop the cron service"},
# {"command": "systemctl restart cron", "description": "Restart the cron service"},


