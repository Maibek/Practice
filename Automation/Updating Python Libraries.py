import subprocess

# pipDisplay список питонов, которые нужно обновить
com_list_o = 'pip list -o'
# Выполнить команду и вернуть результат
p = subprocess.Popen(com_list_o, shell=True, stdout=subprocess.PIPE)
# Возьмите команду для возврата результата, результатом является двоичная строка, которая содержит весь контент, который мы показали после выполнения списка пипсов -o выше
out = p.communicate()[0]
# Бинарный в строку UTF-8
out = str(out, 'utf-8')

# Вырежьте имя пакета для обновления и сохраните его в списке
need_update = []
for i in out.splitlines()[2:]:
    need_update.append(i.split(' ')[0])

# Выполнить команду обновления, принять один пакет за раз, pip поддерживает только один пакет и одно обновление пакета
for nu in need_update:
    com_update = 'pip install -U {py}'.format(py=nu)
    print('Исключая заказ:', com_update)
    subprocess.call(com_update)
    print("---------- {com} Конец выполнения ----------- \ n".format(com=com_update))


print('Проверить наличие обновлений:')
subprocess.call(com_list_o)