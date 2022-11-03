# import time

"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        n1 = 1
        n2 = 1
        cont = 2
        while cont < n:
            a = n2 + n1
            n1 = n2
            n2 = a
            cont += 1
        return n2


tini1 = time.time()
# fibonacci(1000000)
tfin1 = time.time()
print(tfin1 - tini1)

##for i in range(0, 11):
##    print(fibonacci(i))

##numeros = 0
# for i in range(1, 20001):
#    numeros += 1
# print(fibonacci(i))

# print(" ")
# print(numeros)


tini = time.perf_counter()


def fibonacciIterative(n):
    if n < 0:
        raise ValueError("n must be positive")
    n1 = 0
    n2 = 1
    nth = n1 + n2
    for _ in range(n):
        n1 = n2
        n2 = nth
        nth = n1 + n2
    return n1


# fibonacciIterative(1000000)
# print(n1,n2,nth)

def test_fibonacci_of_12():
    expected = 144
    actual = fibonacci(12)
    # actual = fibonacciIterative(12)
    if actual == expected:
        print("OK!")
    else:
        print("Fail")


# test_fibonacci_of_12()


try:
    resultado = fibonacciIterative(-9)
    print(resultado)
except ValueError:
    print("Ha sucedido un error")
except AssertionError:
    print(" ")
except Exception:
    print(" ")


# Así hago para capturar errores

"""


def fibonacci2(n):
    if n < 2: return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)


"""
for i in range(1000):
    resultado = fibonacci2(i)
    print(i,resultado)
"""


# En el gitbush tenemos que poner cd buscar directorio
# Después ponemos  $ time python main.py
# Con esto podemos medir el tiempo


def magia_negra(n):
    cache = {}
    if n<0:
        raise ValueError("Argumento negativo")
    elif n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        res = magia_negra(n - 1) + magia_negra(n - 2)
        cache[n] = res
    return res


print(magia_negra(99))
