import numpy as np

calculated_primes = {}
is_prime_eratosthene={1: False} # dictionary initialized with 1 is not a prime

def sum_for_list(arr):
    primes = set()
    abs_arr = [abs(num) for num in arr]
    sieve_of_eratosthenes(max(abs_arr))
    #print(sorted(is_prime_eratosthene.items()))
    for num in abs_arr:
        if is_prime_eratosthene[num]:
            primes.add(num)
            continue
        for i in range(2, num+1):
            if is_prime_eratosthene[i] and num % i == 0:
                primes.add(i)
                #print(f"{primes=}, {i=}")

    result = []
    for p in sorted(primes):
        prime_sum = sum(num for num in arr if num % p == 0)
        result.append([p, prime_sum])
    return result

def sieve_of_eratosthenes(limit):
    for i in range(2, int(limit)+1):
        is_prime_eratosthene[i] = True
    for i in range(2, int(np.sqrt(limit)) + 1):
        if is_prime_eratosthene[i]:
            for j in range(i*i, limit+1, i):
                is_prime_eratosthene[j]=False