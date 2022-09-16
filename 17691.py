a = 9
temp = ''
s1 = ''
while True:
    b = a % 2
    a = a // 2
    temp += str(b)
    if a == 0:
        break
while True:
    if len(temp) == 5:
        break
    temp += '0'
s1 += temp[::-1]
print(s1)

