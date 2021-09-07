n=int(input())
word=input()

strings=[]
strings_including_word=[]

for i in range(n):
    text=input()
    strings.append(text)
    if word in text:
        strings_including_word.append(text)

print(strings)
print(strings_including_word)