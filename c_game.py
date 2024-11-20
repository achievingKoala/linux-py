import random
from query_csv import query_joined_data, query_fuzzy_data,query_exclude_data, query_random_data
import query_csv
from record_csv import update_count_csv

# command_a=['k8s_cluster_info_commands', 'k8s_resource_management_commands', 'k8s_deployment_management_commands', 'k8s_pod_management_commands']
# command_all=['net_', 'net_low_frequency_commands','process_commands']
# command_all=['package_commands']
rowC = 7
# command_all=['system_structure']
# command_all=['file_']

command_all=['user_group']
command_all=['process_']

command_all=['net_']
command_all=['sed_id', 'awk_', 'cut_']
command_all=['uniq_', 'cat_', 'tr_']
command_all=['grep_']
command_all=['file_ln', 'file_locate', 'find_']

command_all=['shell_var', 'shell_cond']
command_all=['shell_loop', 'shell_dic']
command_all=['system_structure', 'service_commands']
command_all=['desk_file', 'file_ln', 'file_locate']
command_all=['command_usage']
command_all=['cron_c']

# command_all=['docker']
command_all= query_csv.query_min_data()
print(command_all)
commands = query_joined_data(command_group = command_all[0:2], limit = rowC)
# commands = query_fuzzy_data(command_all, limit = rowC)
# commands = query_exclude_data()


def print_colored(word, wordColor, end='\n'):
    color_codes = {
        'green': "\033[92m",
        'red': "\033[91m",
        'blue': "\033[94m",
        'yellow': "\033[93m",
        'cyan': "\033[96m",
        'magenta': "\033[95m"
    }
    reset_code = "\033[0m"
    
    if wordColor in color_codes:
        print(f"{color_codes[wordColor]}{word}{reset_code}", end=end)
    else:
        print(word, end=end)  # Default to printing the word without color

def quiz_user():
    score = 0
    total_questions =  rowC if (len(commands) >= rowC) else len(commands)

    questions = random.sample(commands, total_questions)  # Get unique questions
    # questions = commands 

    for index, question in enumerate(questions):  # Iterate over unique questions
        while True:
            print_colored("Question", 'red', end = ':')
            print(f"{index + 1}: Command description: '{question['description']}'", end=', ')
            print(f"count: {question['pCount']}")
            user_answer = input("What is the command? ")
            
            if user_answer.lower() == 's':
                print_colored("skip", "blue")
                update_count_csv(question['id'], question['command'], False)
                break
            if user_answer.lower() == question['command'].lower():
                print_colored("Correct!", "green")
                score += 1
                update_count_csv(question['id'], question['command'], True)
                break
            else:
                print_colored(f"     The command is: {question['command']}", "blue")

    print(f"Your final score: {score}/{total_questions}")
    # print_result(query_joined_data(command_group = command_a))

def print_result(res):
    for item in res:
        print(item)

if __name__ == "__main__":
    print("Welcome to the Linux Commands Quiz Game!")
    quiz_user()
