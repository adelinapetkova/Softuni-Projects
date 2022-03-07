class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = {'com', 'bg', 'org', 'net'}

while True:
    email = input()
    if email == 'End':
        break

    name = ''
    domain_name = ''

    if '@' in email:
        name, domain_name = email.split('@')
    else:
        raise MustContainAtSymbolError('Email must contain @')

    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    parts_of_domain_name = domain_name.split('.')
    if len(parts_of_domain_name)<2:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    domain=parts_of_domain_name[-1]
    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
