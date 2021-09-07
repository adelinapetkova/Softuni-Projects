words = input().split()
word = input()

palindromes = [el for el in words if el == el[::-1]]
print(palindromes)

number = words.count(word)
print(f'Found palindrome {number} times')
