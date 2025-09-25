n=int (input("Enter the number : " ))
original_num=n
result=0
while n!=0:
    digit=n%10
    result=result+digit**3
    n=n//10


if(original_num==result) :
    print("armstrong number")  
else:
    print("not armstrong number")    