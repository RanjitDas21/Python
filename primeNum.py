n = int(input("Enter the valu of n: "))
temp = 0

for i in range(2,n):
    if(n % i == 0):
        temp = temp + 1

if(temp == 0):
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")            