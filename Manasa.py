__author__ = 'rfischer'

T = input()

for i in range(0, T):
    n = input()
    a = input()
    b = input()

    #m = [a] * (n - 1)
    s = set()
    m = n - 1
    for j in range(0, n):
        s.add(a * (m - j) + b * (j))
    print str(sorted(s)).strip('[]').replace(',', '')

