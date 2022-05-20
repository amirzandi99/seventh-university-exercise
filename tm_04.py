def sort(array, z):
    for i in range(z):
        mx = i
        for j in range(i+1,z):
            if(array[mx] > array[j]):
                mx = j
        temp = array[mx]
        array[mx] = array[i]
        array[i] = temp
# 
x = []
n = int(input("input count    : "))
print()
for i in range(n):
    print(f"input number {i+1} : ",end='')
    a = int(input())
    x.append(a)
sort(x, n)
print("\nafter sort : ", end='')
for i in range(n):
    print(x[i], end=' ')
print()