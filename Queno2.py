# Write a python script to print first N natural numbers
a=int(input("Enter a number: "))
b=1
while b<=a:
    if b==0 or a==0:
        break
    print(b)
    b=b+1
   