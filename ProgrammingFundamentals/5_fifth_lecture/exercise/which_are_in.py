sequence_1=input().split(', ')
sequence_2=input().split(', ')
result=[]

for word_1 in sequence_1:
    for word_2 in sequence_2:
        if word_1 in word_2:
            result.append(word_1)
            break

print(result)