st=input("Enter a string:").lower()
c=st[0]
st=st.replace(c,'$')
st=c+st[1:]
print(st)

