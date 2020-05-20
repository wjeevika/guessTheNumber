from random import *
n = randint(1,10)
c = 3
i = 0
while c!=0:
    print(f"you have {c} lives")
    i = int(input("Guess any no. between 1-10 = "))
    c-=1
    if i<n:
        print("your no. is smaller")
    elif i>n:
        print("your no. is greater")
    else:
        print("Congratulations! no. = ",i)
        break
if c==0 and n!=i:
    print("You failed")
    print("Correct no = ",n)
