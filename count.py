"""
Counts the number of words
"""

cnt = 0
while True:

    l = raw_input()
    if not l: break;
    cnt += len(l.split(' '))
if cnt:
    print cnt, 1 / cnt
else:
    print cnt, "Inf"
