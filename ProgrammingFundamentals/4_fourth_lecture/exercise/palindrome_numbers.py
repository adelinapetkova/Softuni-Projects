list_of_integers=input().split(', ')

def checking_for_palindromes(list):
    for element in list_of_integers:
        is_palindrome = False
        new_number = ''
        for i in range(len(element)-1,-1,-1):
          new_number+=str(element[i])
        if int(new_number)==int(element):
           is_palindrome=True
        print(is_palindrome)


checking_for_palindromes(list_of_integers)
