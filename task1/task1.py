import argparse

s = []
v = []
n = 0
m = 0

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n")
parser.add_argument("-m", "--m")
args = parser.parse_args()
options = [args.n, args.m]

n = int(args.n)
m = int(args.m)

for i in range(1, n + 1):
    s.append(i)
for e in range(m):
    v.append(e)

a = [str(x) for x in s] * n
b = []
c = []
count = 0

for j in range(n):
    y = list(a[count:(len(v) + count)])
    b.append(y)
    c.append(y[0])
    if c[0] == y[-1]:
        break
    count += (len(v) - 1)
    
print("".join(c))


