#Problem4.Find the sum of all the prime below 1000.
sum=0

for x in range(2,1000):
    prime=True

    for y in range(2,x):
        if x%y==0:
            prime=False
            break
    if prime:
        sum=sum+x

print("Total sum : ",sum)

