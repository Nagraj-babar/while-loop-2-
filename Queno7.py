# Write a python script to print first N even natural numbers in reverse order
a=int(input("Enter a number: "))
while a>0:
    if a%2==0:
        print(a)
    a=a-1    