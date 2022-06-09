import re
x = '[@]+[a-zA-Z]+[0-9]'
y = input('Username: ')
if re.findall(x,y):
    print('pass')
else:
    print('Failed')