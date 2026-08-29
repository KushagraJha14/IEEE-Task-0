def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        # The else block associated with a for loop executes ONLY when 
        # the loop completes all its iterations naturally without hitting a 'break' statement.
        return True
    
    return False

n = int(input().strip())


print(is_prime(n))


primes = []
for i in range(2, n + 1):
    if is_prime(i):
        primes.append(str(i))
print(" ".join(primes))