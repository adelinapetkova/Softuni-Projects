passw = input()


def password_validator(password):
   is_valid=True
   digits = 0
   if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid=False
   for element in password:
        if 65 <= ord(element) <= 90 or 97 <= ord(element) <= 122 or 48 <= ord(element) <= 57:
            pass
        else:
            print('Password must consist only of letters and digits')
            is_valid=False
            break
   for character in password:
        if 48 <= ord(character) <= 57:
            digits += 1
   if digits < 2:
        print('Password must have at least 2 digits')
        is_valid=False
   if is_valid:
        print('Password is valid')


password_validator(passw)
