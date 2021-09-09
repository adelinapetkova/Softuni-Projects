class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'

info=input()
emails=[]

while not info=='Stop':
    sender, receiver, content=info.split()
    email=Email(sender,receiver,content)
    emails.append(email)
    info=input()

indices=[int(el) for el in input().split(', ')]

for el in emails:
    if emails.index(el) in indices:
        Email.send(el)
    print(Email.get_info(el))
