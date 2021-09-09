words=[el.lower() for el in input().split()]
my_words={}

for word in words:
    if word not in my_words:
        my_words[word]=1
    else:
        my_words[word]+=1

for w, q in my_words.items():
    if q % 2 == 1:
        print(w,end=' ')