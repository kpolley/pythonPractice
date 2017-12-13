import time

mem = {}

def factorial(n):

    if(n == 0):
        return 1

    if n not in mem:
        mem[n] = (n*factorial(n-1))

    return mem[n]

def bruteForce(n):
    if n == 0:
        return 1
    return n * bruteForce(n-1)

start1 = time.time()
fact = bruteForce(100)
end1 = time.time()
print(fact);
print("TIME BRUTE FORCE:", end1-start1)

start2 = time.time()
fact = factorial(10)
end2 = time.time()
print(fact);
print("TIME MEMOIZED:", end2-start2)

print(mem)
