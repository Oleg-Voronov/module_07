team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 15520.5
team2_time = 21530.3
tasks_total =score_1 + score_2
time_avg = (team1_time + team2_time) / (score_1 + score_2)

def ch_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result ='победа команды ' + team1
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result ='победа команды ' + team2
    else:
        result = 'Ничья!'
    return result

challenge_result = ch_result()

# %
print('В команде %s участников %s' %(team1 ,team1_num))
print('Итого сегодня в командах участников: %s в %s' %(team1_num,team2_num))

# format()
print('Команда {} решила задач: {}!'.format(team2,score_2))
print('{} решили задачи за {} с !'.format(team2,team2_time))

# f-строки
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунд на задачу!')
