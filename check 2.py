import re

file = open('scheme representation.txt','r')

pat = re.compile('^[gwAQ]+$')

while True:
    code = file.read(2)
    
    if code == '':
        break;

    if not pat.match(code[1]):
        print('Error')