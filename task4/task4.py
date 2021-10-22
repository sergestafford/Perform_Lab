# python task4.py -n=1.txt

import argparse

n = []

parser = argparse.ArgumentParser(description="task4", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-n", type=argparse.FileType('r'), help="1.txt")
args = parser.parse_args()
options = [args.n]
file_1 = args.n

with open('1.txt', 'r'):
    while True:
        line = file_1.readline().split()
        n.append(line)
        if not line:
            break
        file_1.close

n = sum(n, [])
nums = [int(x) for x in n]

m = sorted(nums)[len(nums) // 2]
print(sum(abs(v - m) for v in nums))