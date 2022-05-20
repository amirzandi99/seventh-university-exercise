precinct = [1, 2, 3, 4, 5]
cand_A = [192, 147, 186, 114, 267]
cand_B = [48, 90, 12, 21, 13]
cand_C = [206, 312, 121, 408, 382]
cand_D = [37, 21, 38, 39, 29]
sumCan = []
Percent = []
Percent_show = []
sum_p = 0
win = 0
# 
print ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("precinct","Candidate A","Candidate B","Candidate C","Candidate D","results","Percent"))
for i in range(105):
    print("-",end='')
print()
for i in range(len(precinct)):
    s = cand_A[i] + cand_B[i] + cand_C[i] + cand_D[i]
    sumCan.append(s)
    sum_p += s
for i in range(len(precinct)):
    s = (sumCan[i] * 100) / sum_p
    Percent.append(s)
    t = "{:.2f}".format(s)
    Percent_show.append(t)
for i in range(len(precinct)):
    if(Percent[i] > 50):
        win = precinct[i]
    print ("   {:<15} {:<15} {:<15} {:<15} {:<14} {:<14} {:<15}".format(precinct[i],cand_A[i],cand_B[i],cand_C[i],cand_D[i],sumCan[i],Percent_show[i]))
if(win):
    print(f"\n\nwinner is precinct {win}")
else:
    cand1 = Percent[0]
    prec1 = 1
    for i in range(len(precinct)):
        if(cand1 < Percent[i]):
            cand1 = Percent[i]
            prec1 = precinct[i]
    cand2 = Percent[0]
    prec2 = 1
    for i in range(len(precinct)):
        if(cand2 < Percent[i] and Percent[i] < cand1):
            cand2 = Percent[i]
            prec2 = precinct[i]
    print("\n\ntwo Candidates is")
    print(f"  {prec1} : {cand1}")
    print(f"  {prec2} : {cand2}")
# 
# 
print("\n\n\n")
# 
# 
cand_C[3] = 108
sumCan = []
Percent = []
Percent_show = []
sum_p = 0
win = 0
# 
print ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("precinct","Candidate A","Candidate B","Candidate C","Candidate D","results","Percent"))
for i in range(105):
    print("-",end='')
print()
for i in range(len(precinct)):
    s = cand_A[i] + cand_B[i] + cand_C[i] + cand_D[i]
    sumCan.append(s)
    sum_p += s
for i in range(len(precinct)):
    s = (sumCan[i] * 100) / sum_p
    Percent.append(s)
    t = "{:.2f}".format(s)
    Percent_show.append(t)
for i in range(len(precinct)):
    if(Percent[i] > 50):
        win = precinct[i]
    print ("   {:<15} {:<15} {:<15} {:<15} {:<14} {:<14} {:<15}".format(precinct[i],cand_A[i],cand_B[i],cand_C[i],cand_D[i],sumCan[i],Percent_show[i]))
if(win):
    print(f"\n\nwinner is precinct {win}")
else:
    cand1 = Percent[0]
    prec1 = 1
    for i in range(len(precinct)):
        if(cand1 < Percent[i]):
            cand1 = Percent[i]
            prec1 = precinct[i]
    cand2 = Percent[0]
    prec2 = 1
    for i in range(len(precinct)):
        if(cand2 < Percent[i] and Percent[i] < cand1):
            cand2 = Percent[i]
            prec2 = precinct[i]
    print("\n\ntwo Candidates is")
    print(f"  {prec1} : {cand1}")
    print(f"  {prec2} : {cand2}")