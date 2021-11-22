import base64

file = open('scheme representation.txt','r')
wfile = open('right file','wb')

while True:
    code = file.read(2)
    
    if code == '':
        break;

    wfile.write(base64.b64decode(code + '=='))

wfile.close()