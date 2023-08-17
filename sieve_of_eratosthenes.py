import numpy as np
def sieve_of_eratosthenes(limit):
    for i in range(1, int(limit)+1):
        if i not in is_prime_eratosthene:
            is_prime_eratosthene[i]=True
            for j in range(i*2, limit+1, i):
                is_prime_eratosthene[j]=False 


def is_prime(n):
    global highest_prime
    if n in calculated_primes:
        return calculated_primes[n]
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            calculated_primes[n] = False
            return False
    calculated_primes[n] = True
    return True

calculated_primes = {}

prime_factors = set()
def sum_for_list(arr):
    #print(arr)
    primes = set()
    #primes = set(sieve_of_eratosthenes(max(abs(num) for num in arr))) 
    sieve_of_eratosthenes(max(abs(num) for num in arr))
    checked_prime_factor = 2
    for num in arr:
        factors = set()
        if num < 0:
            num = abs(num)
        if is_prime(num):
            primes.add(num)
            continue
        for i in range(2, num + 1):
            flag = True
            for f in factors:
                if i % f == 0:
                    flag = False
            if flag:
                #print(f"i:{i} num:{num}")
                #checked_prime_factor = i
                #if is_prime(i) and num % i == 0:
                print(sorted(is_prime_eratosthene))
                if is_prime_eratosthene[i] and num % i == 0:
                    
                    primes.add(i)
                    factors.add(i)
                    #print(f"{primes=}, {i=}")

    result = []
    for p in sorted(primes):
        prime_sum = sum(num for num in arr if num % p == 0)
        result.append([p, prime_sum])
    print(sorted(calculated_primes.items()))
    return result

#def sieve_of_eratosthenes(limit):
#    sieve = [True] * (limit + 1)
#    sieve[0] = sieve[1] = False
#    for num in range(2, int(limit**0.5) + 1):
#        if sieve[num]:
#            for multiple in range(num * num, limit + 1, num):
#                sieve[multiple] = False
#    return [num for num in range(limit + 1) if sieve[num]]

is_prime_eratosthene={1: False} # dictionary initialized with 1 is not a prime

#calculated_primes = is_prime_eratosthene
