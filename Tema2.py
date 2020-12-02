# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
#
# a) suma tuturor numerelor de la [0, n]
#
#
def recursive_function(number):
    if number == 0:
        return 0

    return number + recursive_function(number - 1)


print('Suma tuturor numerelor de la [0, n] este:', end=' ')
print(recursive_function(5))


# b) suma numerelor pare de la [0, n]
def recursive_function2(number1):
    if number1 == 0:
        return 0

    if number1 % 2 == 0:
        return number1 + recursive_function2(number1 - 1)
    else:
        return recursive_function2(number1 - 1)


print('Suma tuturor numerelor pare de la [0, n] este:', end=' ')
print(recursive_function2(8))


# c) suma numerelor impare de la [0. n]
def recursive_function3(number2):
    if number2 == 0:
        return 0

    if number2 % 2 == 1:
        return number2 + recursive_function3(number2 - 1)
    else:
        return recursive_function3(number2 - 1)


print('Suma tuturor numerelor impare de la [0, n] este:', end=' ')
print(recursive_function3(7))


# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0.
#
#
def my_function(used_number):
    try:
        my_int = int(used_number)
    except ValueError:
        return 0
    return my_int


print('Elementul citit de la tastatura este:', end=' ')
number3 = input()
print('Valoarea returnata de functie este:', end=' ')
print(my_function(number3))


# Să se scrie o funcție care primește un număr nedefinit de parametrii și
# să se calculeze suma parametrilor care reprezintă numere întregi sau reale.
#
def your_function(*args, **kwargs):
    suma = 0
    if not args:
        return 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            suma = suma + i

    return suma


print('Suma tuturor parametrilor intregi sau reali din functie este:', end=' ')
print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print('Suma tuturor parametrilor intregi sau reali din functie este:', end=' ')
print(your_function())
print('Suma tuturor parametrilor intregi sau reali din functie este:', end=' ')
print(your_function(2, 4, 'abc', param_1=2))
