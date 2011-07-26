cnt = 0
while True:

    l = raw_input()
    if not l: break;
    cnt += len(l.split(' '))
print cnt
