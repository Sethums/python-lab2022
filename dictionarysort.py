d={'acd':1,'abw':9,'bc':2,'bd':3}
print(d.items())
z=list(d.items())
z.sort()

print("Ascending list:",z)
k=list(d.keys())
k.sort(reverse=True)

print("Descending list:",k)
