#assingment 2
#task 1

a=int(input('Enter a Number: '))
cal=a%2
if(cal==0):
    print(f"{a} is a even number")
else:
    print(f"{a} is a odd number")

#TASK 2
summ=0
n=list(range(1,51))
for i in n:
     summ+=i

print(f"The sum of numbers from 1 to 50 is: {summ}")