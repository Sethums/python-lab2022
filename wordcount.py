s=input("Enter a sentence:").lower()
c=[x for x in s.split() if x.isalpha()]
print(len(c))
