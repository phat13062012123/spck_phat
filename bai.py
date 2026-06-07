n = int(input("Nhập một số nguyên dương: "))
a = []
u = []
for e in range( 1, n+1 ):
    a.append(input("Nhập phần tử thứ {}: ".format(e)))
for i in range( 1, e+1 ):
    if n % i == 0:
        u.append(i)
        m = max(u)
print("Ước số lớn nhất của {} là: {}".format(n, m))