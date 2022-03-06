final=int(input('Enter final year:'))
for i in range(2022,final):
    if i%4==0 and (i%100!=0 or i%400==0):
        print(i,end=" ")
