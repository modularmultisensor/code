__author__ = 'Matt Cordoba'
s = "0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f \n \
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- \n \
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n \
20: -- -- -- 23 -- -- -- -- -- -- -- -- -- -- -- -- \n \
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n \
40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- -- \n \
50: -- -- -- -- UU UU UU UU -- -- -- -- -- -- -- -- \n \
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n \
70: -- -- -- -- -- -- -- --"
from ast import literal_eval
foundAddresses = []
lines = s.split('\n')[1:] #remove row header1
for l in lines:
    l = l.strip() #remove white space on ends
    spots = l.split(' ')[1:] #remove column header
    for s in spots:
        s = s.strip()
        if(s != 'UU' and s != '--' and s != ''):
            foundAddresses.append(literal_eval('0x' + s))
print(foundAddresses)