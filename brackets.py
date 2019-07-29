a = []
b = 0
c = 0
n = 4

def A(i):
    global b, c, n
    if i == 2 * n:
        print(a)

    if c < n:
        a.append('(')
        b += 1
        c += 1
        A(i+1)
        a.pop()
        b -= 1
        c -= 1

    if b:
        b -= 1
        a.append(')')
        A(i+1)
        a.pop()
        b += 1



A(0)