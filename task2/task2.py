# python task2.py -f=1.txt -t=2.txt

import argparse

cent_rad = []
coords = []

parser = argparse.ArgumentParser(description="task2", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-f", type=argparse.FileType('r'), help="1.txt")
parser.add_argument("-t", type=argparse.FileType('r'), help="2.txt")
args = parser.parse_args()
options = [args.f, args.t]

file_1 = args.f
file_2 = args.t

with open('1.txt', 'r'):
    while True:
        line = file_1.readline().split()
        cent_rad.append(line)
        if not line:
            break
        file_1.close

with open('2.txt', 'r'):
    while True:
        line = file_2.readline().split()
        coords.append(line)
        if not line:
            break
        file_2.close

center = cent_rad[0]
center = list(center)
x = float(center[0])
y = float(center[1])
r = cent_rad[1]
r = list(r)
r = float(r[0])

n = 0
for e in range(1, len(coords)): 
    if n <= 100:
        x_c = float(coords[n][0])
        y_c = float(coords[n][1]) 
        point = (x - x_c) ** 2 + (y - y_c) ** 2
        if point < r * r:  
            print('1', '\n')  # Точка внутри круга
        elif point == r * r:  
            print('0', '\n')  # Точка на окружности
        elif point > r * r:       
            print('2', '\n')  # Точка не принадлежит кругу
        n += 1

