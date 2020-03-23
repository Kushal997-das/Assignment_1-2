a=''
s = input('Please enter a string: ')
count = 1
s = s.lower()
for char1 in s:
    if count % 2 == 0:
        a +=char1.upper()
        count += 1
    else:
        a += char1
        count += 1
print(a)
