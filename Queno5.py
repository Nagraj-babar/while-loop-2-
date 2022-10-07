# Write a python script to print first N odd natural numbers in reverse order
a=int(input("enter a number: "))
while a>0:
    if a%2!=0:
        print(a)
    a=a-1    
