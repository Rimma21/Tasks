a = 5/2
print(a)
# 2.5
print(1 // 3)
# 0
print(3 // 3)
# 1
print(29 // 3)
# 9
print(1 % 3) # ближайшее число, которое нацело делится на 3 - это ноль
# 1
print(3 % 3) # в этом примере сам делитель может нацело разделиться
# 0
print(29 % 3) # здесь ближайшее число - 27, и поэтому результат 29-27=2
# 2
print ((31 % 2) + (-31 % 2))
print (13 % -3 * 3 - 3**2)
print(round(11*2.5/3, 2))
print(round((3.14159**0.5)/2))
s = "Hello!"

print(s[0])
# H

print(s[4])
# o
colors = 'red blue green'

print(colors.split())
# ['red', 'blue', 'green']
a = "1 2 3 4 5 6"
print(a.split())
numbers = input("1 2 3 4 5 6")

numbers_split = numbers.split()
numbers_lines = "\n".join(numbers_split)

print(numbers_lines)
pi = 31.4159265
print ("%.4e" % (pi))

