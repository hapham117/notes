import csv
import re
import operator


per_user = {}
error_count = {}

def add_user(item, list):
    if item not in list:
        list[item] = {
            'username': item,
            'INFO': 0,
            'ERROR': 0
        }

with open('syslog.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        error_check = re.search(r"ticky: ERROR [\w ]*", line)
        if error_check:
            error = re.search(r"ERROR (.*) \((.*)\)", line)
            error.groups()
            error_type, user = error[1], error[2]
            
            if error_type not in error_count:
                error_count[error_type] = 0
            error_count[error_type] += 1
            
            add_user(user, per_user)
            per_user[user]['ERROR'] += 1
            continue

        info_check = re.search(r"ticky: INFO [\w ]*", line)
        if info_check:
            info = re.search(r"INFO (.*) \((.*)\)", line)
            info.groups()
            
            info_type, user = info[1], info[2]
            add_user(user, per_user)
            per_user[user]['INFO'] += 1
            
with open('error_message.csv', 'w', newline='') as file:
    sorted_error_list = sorted(error_count.items(), key=operator.itemgetter(1), reverse=True)
    writer = csv.writer(file)
    writer.writerow(['Error', 'Count'])
    writer.writerows(sorted_error_list)
    
with open('user_statistics.csv', 'w', newline='') as file:
    sorted_user_list = sorted(per_user.items(), key=operator.itemgetter(0))
    writer = csv.writer(file)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    for user in sorted_user_list:
        user = user[1]
        writer.writerow([user['username'], user['INFO'], user['ERROR']])        