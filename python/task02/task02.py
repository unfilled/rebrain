log = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'

#1.2. Выделите и выведите на экран дату и время
print(log[:15]) 
#1.3. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог
print(log[log.find('s'):log.find(']:')+1])
#1.4. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран
print(log.replace('ideapad', 'PC-12092'))
#1.5. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
print(log.find('failed'))
#1.6. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных)
print(log.upper().count('S'))
#1.7. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран
print(int(log[7:9]) + int(log[10:12]) + int(log[13:15]))

log = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
#The PC "<имя ПК>" recive message from service "<имя сервиса>" what says "<сообщение>" because "<причина ошибки>" at <дата, время>
PC = log[log.find('i'):log.find(' ', log.find('i'))] 
srvc = log[log.find(PC[-1] + ' ') + 2: log.find(':', log.find(PC[-1] + ' ') + 2)]
msg = log[log.find(': ') + 2:log.find(':', log.find(': ') + 2)]
rsn = log[-1 * log[::-1].find(':') + 1:]
dt = log[:15]

print(f'The PC "{PC}" recive message from service "{srvc}" what says "{msg}" because "{rsn}" at {dt}')