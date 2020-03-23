s=input("enter a string")
no_of_words=len(s.split())
no_of_characters=len(s)
percentage_characters=0
for i in s:
    if i.isalnum():
        percentage_characters+=1
print("number_of_words"+str(no_of_words))
print('no_of_characters',no_of_characters)
print("percentage_characters",percentage_characters*100/len(s),'%')
