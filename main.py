import json
import datetime

# Reading data from JSON
with open('todos.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Now date
today = datetime.datetime.today()
day = today.strftime('%d.%m.%Y %H:%M')
f_day = today.strftime('%Y-%m-%dT%H-%M')

result = {}


# Data addition function
def adding_data():
    for u in data:  # sorting json data
        if 'userId' not in u:
            continue
        if u['userId'] not in result:
            result[u['userId']] = {'comp': [], 'uncomp': []}
        if len(u['title']) > 50:
            title = u['title'][:50] + '...'
        else:
            title = u['title']
        if u['completed']:
            result[u['userId']]['comp'].append(title)
        else:
            result[u['userId']]['uncomp'].append(title)
    return result


# Print function
def print_tasks():
    i = 0  # count
    for u in result:  # write to files
        i += 1
        first_line = '# Сотрудник №' + str(u) + '\n'
        four_line = '## Завершенные задачи:\n' + '\n'.join(result[u]['comp'])
        five_line = '\n## Незавершенные задачи:\n' + '\n'.join(result[u]['uncomp'])
        with open(str(u) + '_' + f_day + '.txt', 'w', encoding='utf-8') as file:
            file.write(first_line + day + '\n\n' + four_line + '\n' + five_line)

    print('Успешно созданно ' + str(i) + ' отчетов')


adding_data()
print_tasks()
