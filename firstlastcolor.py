c=input("Enter color name with commas:").split(',')
print("Alternate colors are:\n",*c[0::2],end=",")
