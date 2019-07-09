#Algorithm for conversion from binary to decimal
binary=str(input("Enter any binary number : "))
flag = False
for each in binary:
    if each!='0' and each!='1':
        print("Error in input")
        flag = False
        break
    else:
        flag = True
if flag == True:
    result = 0
    exp = len(binary)-1
    for x in range(0,len(binary)):
        result = int(binary[x])*(2**exp)+result
        exp-=1
    print(result)
   
#Algorithm for Conversion from Decimal System to Binary System in python 3x:
num = int (input ("Enter any positive integer : "))
binary = []
while num!=1:
    binary.append(num%2)
    num=num//2
binary.reverse()
answer = 1
for x in binary:
    answer = answer*10+x
print("Answer is :" +str(answer))
