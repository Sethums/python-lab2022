inf=False
try:
    inf=open('abcd.txt')
    line=inf.readlines()
    line.sort(key=len)
    l=len(line[-1])
    for x in line:
        if len(x)==l:
            print(x)
except IOError as io:
    print(io)
finally:
    if inf:
        inf.close()
