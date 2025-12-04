num = int(input("Введите целое число: "))
if num < 0:
    print(abs(num))
elif num == 0:
    print(1)
else:
    print(num)

s = input("Введите произвольную строку:") 
if '.' in s or ',' in s: ...
else:
    print(False)

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: ")) 
if a % 3 == 0 and b % 3 == 0:
    print(True)
elif a % 3 == 0 or b % 3 == 0:
     print("Одно число делится на 3")
else:
    print(False)
  

num = int(input("Введите число:"))
if num < 0:
    pass
elif num > 100:
    print("*")
else:
    print("*" * num)

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
if str1 == str2:
    print(True)
else:
    print(False) 

r = int(input("Введите значение r: "))
g = int(input("Введите значение g: "))
b = int(input("Введите значение b: "))
if r == 0  and g == 0 and b == 0:
    print("Черный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b ==255:
    print("Синий цвет")
else:
    print("Нет цвета")


number = float(input("Введите число: "))
if number > 0:
   print(number - 1)
   print(number)
   print(number + 1)

filename = int(input("Введите имя файла с расширением: "))
extension = filename.split('.')[-1].lower()
if extension == 'doc' :
   print("World file")
elif extension == 'py' :
   print("Python file")
elif extension == 'txt' :
   print("Text file")
else:
   print("Неизвестное расширение")

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
с = float(input("Введите длину третьей стороны: "))
if a == b == c:
   print("Равносторонний треугольник")
elif a == b  or b == c or a == c:
   print("Равнобедренный треугольник")
else:
   print("Разносторонний треугольник")


text = 'important information in one line'
letter = input("Введите букву: ")
if letter in text:
    print(True)
else:
    print(False)

side1 = float(input("Введите первую сторону: "))
sibe2 = float(input("Введите вторую строну:  "))
if side1 == side2:
    figure = "квадрат"
    area = side1 * side2
else:
    figure = "прямоугольник"
    area = side1 * side2
print(f"Это {figure}, его площадь: {area}")

