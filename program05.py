s=input("enter a string").split()
sum=0
for x in s:
   if not x.isalpha():
            sum=sum+int(x)
print(f"the original string is :{s} and  the sum of the digits is:{sum}")
