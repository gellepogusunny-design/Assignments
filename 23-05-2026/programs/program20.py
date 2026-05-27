lower=int(input("Enter the lower limit of the  interval: "))
upper=int(input("Enter the upper limit of the  interval: "))
for num in range(lower, upper + 1):
   order=len(str(num))
   temp=num
   sum=0
while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
if num==sum:
    print(num)
