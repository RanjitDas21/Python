n = int(input("Enter the n: "))
p = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(p,end=" ")
        p = p+1
    print()    