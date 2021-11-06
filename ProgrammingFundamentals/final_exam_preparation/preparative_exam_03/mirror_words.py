import re

regex = r'(?P<sep>[@|#])(?P<word1>[a-zA-Z]{3,})(?P=sep)(?P=sep)(?P<word2>[a-zA-Z]{3,})(?P=sep)'
text = input()
valid_pairs = 0
valid_pairs_of_words = re.finditer(regex, text)
mirror_words = []

for pair in valid_pairs_of_words:
    valid_pairs += 1
    pairr = ''
    if pair.group('word1') == pair.group('word2')[::-1]:
        pairr += pair.group('word1')
        pairr += ' <=> '
        pairr += pair.group('word2')
        mirror_words.append(pairr)

if valid_pairs==0:
    print('No word pairs found!')
else:
    print(f'{valid_pairs} word pairs found!')

if len(mirror_words)==0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))

