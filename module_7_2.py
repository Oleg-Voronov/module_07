def custom_write(f_name,strings):
    file = open(f_name,'w',encoding='utf-8')
    n = 0 # номер строки
    s_p = {} # взвращаемый словарик
    for str_ in strings:
        pointer = file.tell() # позиция курсора
        n+=1
        s_p.update({(n,pointer):str_})
        file.write(str_)
        file.write('\n')
    file.close()
    return s_p

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!',
    'хм... со второго запуска всё заработало.. :-)'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


