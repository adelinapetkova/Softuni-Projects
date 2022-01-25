def age_assignment(*args, **kwargs):
    names_and_ages={}
    for name in args:
        first_letter=name[0]
        for letter, age in kwargs.items():
            if letter==first_letter:
                names_and_ages[name]=age
                break
    return names_and_ages


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))