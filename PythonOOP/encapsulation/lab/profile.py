class Profile:
    min_username_length=5
    max_username_length=15

    min_password_length=8
    min_uppercase_letters_password=1
    min_digits_password=1

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def username_validator(self, value):
        if not self.min_username_length<=len(value)<=self.max_username_length:
            raise ValueError("The username must be between 5 and 15 characters.")

    def password_validator(self,value):
        error_message="The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
        digits=[d for d in value if d.isdigit()]
        uppercase_letters=[l for l in value if l.isupper()]

        if len(value)<self.min_password_length:
            raise ValueError(error_message)
        elif len(uppercase_letters)<self.min_uppercase_letters_password:
            raise ValueError(error_message)
        elif len(digits)<self.min_digits_password:
            raise ValueError(error_message)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.username_validator(value)
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.password_validator(value)
        self.__password=value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"".join(["*" for _ in range(len(self.__password))])}'


correct_profile = Profile("My_username", "My-password")
print(correct_profile)
