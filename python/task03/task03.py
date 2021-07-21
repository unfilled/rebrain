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

d = {}

## Запросить номер строки
i = input('Input line number: ') ## не проверяю, что а) введено число; б) оно не выходит за границу 

## Заполнить словарь d
log_split = logs[int(i)].split(' ')

d['time'] = ' '.join(log_split[:3])
d['pc_name'] = log_split[3]
d['service_name'] = log_split[4].replace(":", "")
d['message'] = ' '.join(log_split[5:])

## Выведите на экран информацию из текущего словаря 
print(f"{d['pc_name']}: {d['message']}")

## 4.1 Скопировать список
l4_values = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']
## 4.2 Создать список ключей
l4_keys = ['time', 'pc_name', 'service_name', 'message']
## 4.3 Создать словарь из списков
d4 = dict(zip(l4_keys, l4_values))

## 5 Создайте список из словаря, который вы получили в пункте 3 и словаря из пункта 4
l = [d, d4]
## 5 Выведите полученный список на экран
print(l)

## 6 Используя преобразование во множество, выведите список совпадающих значений полученных словарей.
print(set(d.values()) & set(d4.values()))