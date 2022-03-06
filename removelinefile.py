inf=False
try:
    n=int(input("line number:"))
    with open('abcd.txt','r+') as inf:
        line=inf.readlines()
        line.pop(n-1)
        inf.truncate(0)
        inf.seek(0,0)
        inf.writelines(line)
except IOError as io:
    print(io)
finally:
    if inf:
        inf.close()
inf=False
try:
    inf=open('abcd.txt')
    print(inf.read())
except IOError as io:
    print(io)
finally:
    if inf:
        inf.close() 
