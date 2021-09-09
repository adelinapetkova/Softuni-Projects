n = int(input())
synonym_dictionary = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonym_dictionary:
        synonym_dictionary[word] = []
    synonym_dictionary[word].append(synonym)

for key, value in synonym_dictionary.items():
    print(f"{key} - {', '.join(value)}")
