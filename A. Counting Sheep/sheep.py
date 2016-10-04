def count(digit):
    a = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    counter = 1;
    orig_dig = digit
    while(0 in a.values()):
        lastnum = digit
        for i in (str(digit)):
            a[i] = 1
        counter += 1
        digit = orig_dig * counter
        if (digit == lastnum):
            return "INSOMNIA"
    return lastnum 

c = 0
for line in open("A-large-practice.in"):
    if c == 0:
        c += 1
        continue
    print "Case #%d:" % (c), 
    print count(int(line))
    c += 1



