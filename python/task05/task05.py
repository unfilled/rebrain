logs = [
    'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated',
    'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
    'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
    'May 20 11:01:12 PC-00102 PackageKit: daemon start',
    'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
    'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
    'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
    'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
    'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
    'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
    'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'
]

log = []

# 2 Создайте из него список словарей, используя ключи из того же задания.
for rec in logs:
    d = {} 
    log_split = rec.split(' ')
    d['time'] = ' '.join(log_split[:3])
    d['pc_name'] = log_split[3]
    d['service_name'] = log_split[4].replace(":", "")
    d['message'] = ' '.join(log_split[5:])
    log.append(d)

# 3 Выведите на экран список значений <дата/время> всех словарей. Воспользуйтесь списковым включением.
[print(rec['time']) for rec in log]

# 4 Измените словари... В поле 'time' оставьте только время. Выведите значения для поля 'time' всех словарей в списке.
for rec in log:
    rec['date'] = ' '.join(rec['time'].split(' ')[:2])
    rec['time'] = rec['time'].split(' ')[2]
    print (rec['time'])

# 5 Выведите список значений поля 'message' для всех логов, которые записал ПК с именем 'PC0078'
#   Воспользуйтесь списковым включением.
[print (rec['message']) for rec in log if rec['pc_name'] == 'PC0078']

# 6 Превратите список логов в словарь. Ключами в нем будут целые числа от 100 до 110, а значениями - словари логов.
ed = dict(enumerate(log, 100))

# 7 Выведите на экран лог под ключом 104.
print(ed[104])
