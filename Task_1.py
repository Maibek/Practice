print('Этот код может складывать, вычитать, умножать и делить числа.')
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = input('введите арифметический знак:')
def convert():
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c =='/':
        print(a / b)
    else:
        print('Вы ввели неверный знак, попробуйте еще.')
convert()
while True:
    if True:
        a = int(input('Введите снова первое число:'))
        b = int(input('Введите снова второе число:'))
        c = input('введите арифметический знак:')
        convert()
    else:
        break
