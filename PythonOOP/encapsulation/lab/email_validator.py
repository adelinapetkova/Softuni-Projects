import re


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.domains = domains
        self.mails = mails
        self.min_length = min_length

    def __is_name_valid(self, name):
        if len(name)>=self.min_length:
            return True
        return False

    def __is_mail_valid(self,mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        (name, mail, domain)=re.split('[@.]', email)
        if self.__is_mail_valid(mail) and self.__is_domain_valid(domain) and self.__is_name_valid(name):
            return True
        return False


