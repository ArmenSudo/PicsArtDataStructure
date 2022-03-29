from random import randint


# _________________ Prime Numbers Check O(n) ________________________

def is_divisor(a, b):
    return a % b == 0


def find_smallest_divisor1(a, d=2):
    if is_divisor(a, d) or a == 1:
        return d
    return find_smallest_divisor1(a, d + 1)


def is_prime1(n):
    return find_smallest_divisor1(n) == n


print("O(n) -> ", is_prime1(5))


# ___________________________________________________________________


# ________________ Prime Number Check O(sqrt(n)) ____________________

def find_smallest_divisor2(a, d=2):
    if d ** 2 > a:
        return a
    elif is_divisor(a, d):
        return d
    else:
        return find_smallest_divisor2(a, d + 1)


def is_prime2(n):
    return False if n < 2 else find_smallest_divisor2(n) == n


print("O(sqrt(n)) -> ", is_prime2(6))


# ___________________________________________________________________


# __________________ Prime Number check O(log(n)) ___________________


def fermat_test(n):
    a = randint(2, n - 1)
    return (a ** n) % n == a


def fast_prime(n, times=1):
    if n == 2:
        return True
    if n < 2:
        return False
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False


print("O(log(n)) -> ", fast_prime(13))

# ___________________________________________________________________


# ___________________ Prime Check ______________ O(n)

def is_prime_iter(n):
    d = 2
    while d < n:
        if is_divisor(n, d):
            return False
        d += 1
    return True


print("Is Prime O(n) iter -> ", is_prime_iter(19))


# ___________________________________________________
