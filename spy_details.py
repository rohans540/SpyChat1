#importing datetime class
from datetime import datetime
#creating Spy class
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.mode = True
        self.chats = []
        self.current_status_msg = None

#instantiation of Spy
spy = Spy('Bond', 'Mr ', 23, 4.9)

#instantiating friends using class Spy
frnd1 = Spy('Rohan', 'Mr ', 23, 4.9)
frnd2 = Spy('Raju', 'Mr ', 24, 4.2)
frnd3 = Spy('Surbhi', 'Miss ', 23, 4.5)
frnd4 = Spy('Rishav', 'Mr ', 23, 4.8)

#list of friends containing frnd objects
friends = [frnd1, frnd2, frnd3, frnd4]

class Chatmessage:
    def __init__(self, msg, sent_by_me):
        self.msg = msg
        self.time = datetime.now
        self.sent_by_me = sent_by_me