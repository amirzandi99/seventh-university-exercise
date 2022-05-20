# a = 0 7 9 4 0 0 8 0 4 5 0 1
x = 12
a = [int(x) for x in input("input code digit : ").split()]
o = 0
e = 0
for i in range(len(a)-1):
    if(i % 2 == 0):
        e += a[i]
    else:
        o += a[i]
o *= 3
s = (o + e) + (10 - (a[x-2] % 10))
if(s == ((a[1] * 10) + a[2])):
    print("\nTrue")
else:
    print("\nFalse")