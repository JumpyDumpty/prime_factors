import math
def prime_factors(num):
    factor_list = []
    while num % 2 == 0:
        factor_list.append(2)
        num = num/2
    for a in range(3, int(math.sqrt(num))+1, 2):
        while (num % a == 0):
            factor_list.append(int(a))
            num = num / a
    if num > 2:
        factor_list.append(int(num))
    return factor_list

print(prime_factors(20))
print(prime_factors(100))
print(prime_factors(114514))
print(prime_factors(5201314))
//why delete my codes!!!!
