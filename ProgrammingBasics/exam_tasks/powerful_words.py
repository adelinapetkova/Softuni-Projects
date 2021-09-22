import math

word=input()
sum_letters=0
total_sum=0
biggest_sum=-65565865
powerful_word=''
word_lenght=0
first_letter_is_vowel=False

while word!='End of words':
    enumerated_word=enumerate(word)
    word_lenght=len(word)
    for count,letter in enumerated_word:
        ascii=ord(letter)
        sum_letters+=ascii
        if count==0:
           if ascii==65 or ascii==97 or ascii==69 or ascii==101 or ascii==73 or ascii==105 or ascii==79 or ascii==111 or ascii==85 or ascii==117 or ascii==89 or ascii==121:
                first_letter_is_vowel=True
           else:
               first_letter_is_vowel=False
    if first_letter_is_vowel:
        total_sum=sum_letters*word_lenght
    else:
        total_sum=math.floor(sum_letters/word_lenght)
    if total_sum>=biggest_sum:
        biggest_sum=total_sum
        powerful_word=word
    word=input()
    total_sum=0
    sum_letters=0

print(f'The most powerful word is {powerful_word} - {biggest_sum}')