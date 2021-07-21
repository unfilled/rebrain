l = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

i = input("Input device number: ")

device = l[int(i)]

free = (device['total'] - device['used']) / 1024 / 1024 / 1024
free_p = (device['total'] - device['used']) / device['total'] * 100

if free < 10 or free_p < 5:
    print (f"на накопителе {i} критически мало свободного места")
elif free < 30 or free_p < 10:
    print (f"на накопителе {i} мало свободного места")
else:
    print(f"на накопителе {i} достаточно свободного места")