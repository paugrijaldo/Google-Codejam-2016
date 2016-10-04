#pancakes
def p_count(stack):
    prev = ''
    count = 0
    for pancake in stack.rstrip():
        if prev == '' or prev == pancake:
            if prev == '' and pancake == '-':
                count += 1
            prev = pancake
            continue
        elif prev != pancake:
            if prev == '+':
                count += 2
        prev = pancake
    return count

c = 0
for line in open('B-large-practice.in'):
    if c == 0:
        c += 1
        continue
    print "Case #%d:" % (c),
    print p_count(line)
    c += 1
