
a = lambda x, y: print(x/y)
try:
    print('Введите делимое')
    x = int(input())
    print('Введите делитель')
    y = int(input())
    a(x, y)
except ZeroDivisionError:
    print('на ноль делить нельзя!')
except TypeError or ValueError:
    print('это не число!')