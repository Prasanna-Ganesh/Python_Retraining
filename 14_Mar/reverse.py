
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[2].reverse()
print(a)


def rev(a):
    b=a[2].reverse()
    return b

def show():
    a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
    c=rev(a)
    print(c)

show()