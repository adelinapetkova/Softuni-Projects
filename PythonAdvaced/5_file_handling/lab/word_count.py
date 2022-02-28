words_dict={}
words_file=open('words.txt', 'r')
input_file=open('input.txt', 'r')
words=[word.lower() for word in words_file.readlines()[0].split()]
lines=[w for w in input_file.readlines()]
list_of_words=[]
for line in lines:
    input_words=[w for w in line.split()]
    for word in input_words:
        list_of_words.append(word.lower())

for word in words:
    words_dict[word]=0
    for w in list_of_words:
        if word == w:
            words_dict[word]+=1

words_dict=dict(sorted(words_dict.items(), key=lambda x: -x[1]))
for word, value in words_dict.items():
    print(f'{word} - {value}')

