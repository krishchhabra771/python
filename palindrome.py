n=int (input("Enter the number : " ))
original_num=n
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

print(f"Reverse is : {rev}" )
if(original_num==rev) :
    print("palindrome number")  
else:
    print("not palindrome number")    