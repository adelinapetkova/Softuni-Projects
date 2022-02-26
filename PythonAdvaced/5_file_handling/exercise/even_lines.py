file = open('input.txt', 'r')

symbols_to_replace = {'-', ',', '.', '!', '?'}
index=0
while True:
    sentence = file.readline().strip()
    if not sentence:
        break
    if index%2==1:
        index+=1
        continue
    sentence_as_chars=[]
    for l in range(len(sentence)):
        sentence_as_chars.append(sentence[l])
        if sentence_as_chars[l] in symbols_to_replace:
            sentence_as_chars[l]='@'
    index+=1
    sentence=''.join(sentence_as_chars)
    reversed_sentence_words=reversed([w for w in sentence.split()])
    print(' '.join(reversed_sentence_words))

file.close()
