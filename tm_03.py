def sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if(j < len(a)-1):
                if(a[j] > a[j+1]):
                    temp = a[j]
                    a[j] = a[j+1]
                    a[j+1] = temp
    return a
# 
# 
# 
def merge(a1, a2):
    a3 = []
    x1 = len(a1)
    x2 = len(a2)
    x3 = x1 + x2
    k1 = 0
    k2 = 0
    t1 = 0
    t2 = 0
    for i in range(x3):
        if(a1[k1] < a2[k2]):
            a3.append(a1[k1])
            k1 += 1
        elif(a1[k1] > a2[k2]):
            a3.append(a2[k2])
            k2 += 1
        else:
            a3.append(a1[k1])
            a3.append(a2[k2])
            k1 += 1
            k2 += 1
        if(k1 == x1):
            t1 = 0
            break
        if(k2 == x2):
            t2 = 0
            break
    if(t1 == 0):
        while(k2 < x2):
            a3.append(a2[k2])
            k2 += 1
    if(t2 == 0):
        while(k1 < x1):
            a3.append(a1[k1])
            k1 += 1
    tmp = []
    for i in range(len(a3)):
        if(a3[i] in tmp):
            continue
        else:
            tmp.append(a3[i])
    return tmp
# 
# 
# 
l1 = []
l2 = []
l3 = []
print()
n1 = int(input("input count list 1 : "))
for i in range(n1):
    print(f"input list1[{i}] : ", end='')
    x = float(input())
    l1.append(x)
# 
print()
n2 = int(input("input count list 2 : "))
for i in range(n2):
    print(f"input list2[{i}] : ", end='')
    x = float(input())
    l2.append(x)
# 
l1 = sort(l1)
l2 = sort(l2)
l3 = merge(l1,l2)
print("\nresult : ", end='')
for i in range(len(l3)):
    print(f"{l3[i]} ", end='')
print()