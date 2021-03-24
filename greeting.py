
def calc (a, b, c):
    if(a == 'x'):
        return b*c
    elif (a=='-'):
        return b-c
    elif (a=='/'):
        return round(b/c)
    elif(a=='+'):
        return b+c
fstep2 = open("C:/Users/44757/Desktop/Python/step_2.txt",'r')
lines = fstep2.read().splitlines()
a=0
for line in lines:
    fields = line.split(" ")
    a = a + calc(fields[1],int(fields[2]),int(fields[3]))

print("Total value: ",a)

fstep3 = open("C:/Users/44757/Desktop/Python/step_3.txt",'r')
linesStep3 = fstep3.read().splitlines()
list_lineNo = []
for lineStep3 in linesStep3:
    fieldStep3 = lineStep3.split(" ")
    lineNo = 0
    if (fieldStep3[1]=='calc'):
        lineNo = calc(fieldStep3[2],int(fieldStep3[3]),int(fieldStep3[4]))
    else:
        lineNo = fieldStep3[1]
    if lineNo in list_lineNo:
        print("the break line no is: ",lineNo)
        break
    else:
        list_lineNo.append(lineNo)



