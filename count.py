"""
Counts the number of words
"""

ct = 0
while True:

    l = raw_input()
    if not l: break;
    ct += len(l.split(' ')).split(',')
if ct:
    print ct, 1 / ct
else:
    print ct, "Inf"
