import string
import matplotlib.pyplot as plot

file = open('scheme representation.txt','r')

frequencies = {}

for i in range(0,10):
    frequencies[str(i)] = 0
    
for i in list(string.ascii_lowercase):
    frequencies[i] = 0
    
for i in list(string.ascii_uppercase):
    frequencies[i] = 0

frequencies['+'] = 0
frequencies['/'] = 0

while True:
    code = file.read(1)
    
    if code == '':
        break;
    
    frequencies[code] += 1

plot.bar(list(frequencies.keys()), frequencies.values(), color='b')
plot.show()