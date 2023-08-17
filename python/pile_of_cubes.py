def find_nb(m):
    sum = 0
    for n in range(m):
        #print(f"n:{n} m:{m} sum:{sum}")
        sum += n**3
        if sum > m:
            return -1
        #for i in range(n,0,-1):
        #    sum += i**3
            #print(f"n:{n} i:{i} sum:{sum}")
        if m == sum:
            return n