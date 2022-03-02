file = open('text.txt', 'r')
output_file=open('output.txt', 'w')

index=1
while True:
    sentence = file.readline().strip()
    punctuation_marks=0
    spaces=0
    if not sentence:
        break
    for ch in sentence:
        if not ch.isalpha() and not ch==' ':
            punctuation_marks+=1
        elif ch==' ':
            spaces+=1
    output_file.write(f'Line {index}: {sentence} ({len(sentence)-punctuation_marks-spaces})({punctuation_marks})\n')
    print(f'Line {index}: {sentence} ({len(sentence)-punctuation_marks-spaces})({punctuation_marks})')
    index+=1

file.close()
output_file.close()

