import re
a = open('PraktikumASD\quiz\qiuz.txt','r')
x = a.read()
q = re.findall(r'\w+@\w+',x)
print(q)