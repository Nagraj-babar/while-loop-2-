# Write a python script to print first N odd natural numbers
a=int(input("Enter a numer: "))
b=1
while b<=a:
    if b%2!=0:
        print(b)
    b=b+1    