# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 

def SieveOfEratosthenes(n):
    
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for _ in range( n + 1 )]
    print("Iteration Track")
    i = 2
    while i * i < n + 1:
        
        # If prime[i] is not changed, then it is a prime 
        if prime[i] == True:
            print("i: ",i)
            # Update all multiples of i
            for j in range(i * 2, n + 1, i ):
                print("\tj: ", j)
                
                prime[j] = False
        i += 1
        
    #set these two always False
    prime[0]= False
    prime[1]= False

    # Print all prime numbers 
    print("\nPrime numbers from 1 to ",n)
    for _ in range( n + 1 ):
        
        if prime[ _ ]== True:
            
            print(_,end = " ")


SieveOfEratosthenes(int(input('Enter the value of n: ')))