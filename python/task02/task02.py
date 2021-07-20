log = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
splt = log.split(' ')
print('############### 1 ###############')
print()

#1.2. Выделите и выведите на экран дату и время
print(' '.join(splt[:3]))
#1.3. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог
print(splt[3])
#1.4. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран
print(log.replace('ideapad', 'PC-12092'))
#1.5. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
print(log.find('failed'))
#1.6. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных)
print(log.upper().count('S'))
#1.7. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран
print(eval('+'.join(splt[2].split(':'))))

print()
print('############### 2 ###############')
print()

log = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
splt = log.split(': ')
fsplt = splt[0].split(' ')

#The PC "<имя ПК>" recive message from service "<имя сервиса>" what says "<сообщение>" because "<причина ошибки>" at <дата, время>
PC = fsplt[3]
srvc = fsplt[4]
msg = splt[1]
rsn = splt[2]
dt = ' '.join(fsplt[:3])

print(f'The PC "{PC}" recive message from service "{srvc}" what says "{msg}" because "{rsn}" at {dt}')