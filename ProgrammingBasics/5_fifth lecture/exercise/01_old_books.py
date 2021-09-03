searching_for=input()
book=input()
book_is_found=False
checked=0

while book!='No More Books':
    checked += 1
    if book==searching_for:
        book_is_found=True
        checked -= 1
        print(f'You checked {checked} books and found it.')
        break
    book=input()


if book_is_found==False:
    print('The book you search is not here!')
    print(f'You checked {checked} books.')

