import random
from query_csv import query_joined_data, query_fuzzy_data
from record_csv import update_count_csv

# commands = get_commands('grep_commands')
# command_a=['k8s_cluster_info_commands', 'k8s_resource_management_commands', 'k8s_deployment_management_commands', 'k8s_pod_management_commands']
# command_all=['net_high_frequency_commands', 'net_low_frequency_commands','process_commands']
# command_all=['grep_commands','find_commands', 'redhat_package_commands']
# command_all=['sed_commands', 'tr']
command_all=['shell']
commands = query_joined_data(command_group = command_all)
commands = query_fuzzy_data(command_all)

def print_colored(word, wordColor):
    color_codes = {
        'green': "\033[92m",
        'red': "\033[91m",
        'blue': "\033[94m",
    }
    reset_code = "\033[0m"
    
    if wordColor in color_codes:
        print(f"{color_codes[wordColor]}{word}{reset_code}")
    else:
        print(word)  # Default to printing the word without color

def quiz_user():
    score = 0
    total_questions =  5 if (len(commands) >= 5) else len(commands)

    questions = random.sample(commands, total_questions)  # Get unique questions
    # questions = commands 

    for question in questions:  # Iterate over unique questions
        print(f"Command description: '{question['description']}'", end = ',')
        print(f"count: {question['pCount']}")
        user_answer = input("What is the command? ")
        
        if user_answer.lower() == question['command'].lower():
            print_colored("Correct!", "green")
            score += 1
            update_count_csv(question['id'], question['command'], True)
        else:
            print_colored(f"     The command is: {question['command']}", "blue")
            update_count_csv(question['id'], question['command'], False)

    print(f"Your final score: {score}/{total_questions}")
    # print_result(query_joined_data(command_group = command_a))

def print_result(res):
    for item in res:
        print(item)

if __name__ == "__main__":
    print("Welcome to the Linux Commands Quiz Game!")
    quiz_user()
