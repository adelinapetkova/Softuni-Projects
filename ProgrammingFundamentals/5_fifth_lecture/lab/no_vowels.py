text=input()
vowels=['a','e','o','u','i']

result=[]
for letter in text:
    result.append(letter)

print(''.join([el for el in result if el.lower() not in vowels]))

