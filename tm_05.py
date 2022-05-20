t = 6
s = 6
n = 12
for i in range(s,n):
    if(i == 6):
        for j in range(s,n-1):
            print(f"\t{j}", end='')
    else:
        print(f"{t}", end='\t')
        for j in range(s,n-1):
            print(f"{t*j}", end='\t')
        t += 1
    print()