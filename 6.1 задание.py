def invert(input_string):
    a=''
    for i in input_string:
        if 'A' <= i <= 'Z':
            a+=chr(ord(i)+32)
        elif 'А' <= i <= 'Я':
            a+=chr(ord(i)+32)
        else:
            a+=i
    return a
n=input('Введите строку :')
print("Исходная строка ", n)
print("Преобраззованная строка ", invert(n))