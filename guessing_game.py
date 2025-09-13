import random
print("Welcome to Number guessing game")
secret_number=random.randint(1,10)
attempt=0
while True:
    user_num=int(input("Enter the number :"))
    attempt+=1
    if user_num<secret_number:
        print('too low !,Try again')
    elif user_num>secret_number:
        print('too high !,Try again')    
    else:
        print(f"Congratulations!,You have guess the number in {attempt} attempt")    