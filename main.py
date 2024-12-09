# Acivity 1
# from math import sqrt
# no= int(input("Enter a number:"))
# if no>1:
#     for i in range (2, int(sqrt(no)+1)):
#         if no%i==0:
#             print(no,"is not prime number")
#             break
#         else:
#             print(no,"is a prime number")
# else:
#     print(no,"is not a prime number")
# Acivity 2
def primeseive(n):
    prime=[True for i in range(n+1)]
    currentnumber=2
    while (currentnumber *currentnumber<n):
        if (prime[currentnumber]==True):
            for i in range (currentnumber**2,n+1,currentnumber):
                prime[i]=False
        currentnumber+=1
    prime[0]=False
    prime[1]=False
    for p in range (n+1):
        if prime[p]:
            print(p)
n= int(input("Enter a number:"))
primeseive(n)