import base64

dc = {}

with open('dict.txt', 'r') as f:
    rlines = f.readlines()
    for i in rlines:
        res = i[:-1].split(':')
        dc[res[0]] = base64.b64decode(res[1])

with open('scheme.txt', 'r') as fl:
    with open('right file', 'wb') as fr:
        while True:
            row = fl.readline()[:-1]
            if row == '':
                break;
            fr.write(dc[row])