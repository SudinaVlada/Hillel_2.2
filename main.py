_user_input = input("Введіть число: ")
user_input = int(_user_input)
a = user_input // 10000
b = (user_input // 1000) % 10
c = (user_input // 100) % 10
d = (user_input // 10) % 10
e = user_input% 10
print(e, d, c, b, a, sep='')