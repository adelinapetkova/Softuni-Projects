word_1, word_2=input().split()
total_sum=0

if len(word_1)==len(word_2):
    for i in range(len(word_1)):
        total_sum+=ord(word_1[i])*ord(word_2[i])
elif len(word_1)>len(word_2):
    for i in range(len(word_2)):
        total_sum += ord(word_1[i]) * ord(word_2[i])
    for j in range(len(word_2),len(word_1)):
        total_sum+=ord(word_1[j])
else:
    for i in range(len(word_1)):
        total_sum += ord(word_1[i]) * ord(word_2[i])
    for j in range(len(word_1),len(word_2)):
        total_sum+=ord(word_2[j])

print(total_sum)