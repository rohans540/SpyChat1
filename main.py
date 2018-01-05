#spychat application in python
print "Hey there!\n"
print "welcome to spychat world!\nLet's get started"

#reading spy name
spy_name= raw_input("Hey! You must tell me your name first:\n")

#name validation
if len(spy_name)>0:
    print "Welcome '" +spy_name + "' glad to have you back with us\n"

    #asking salutation
    spy_salutation = raw_input("What should i call you Mr or Miss?\n")

    #concatenate salutation and name
    spy_name = spy_salutation + " " + spy_name

    print "Alright '" + spy_name + "' I would like to know a little bit more about you before we proceed...!\njust a minute\n"

#new variables for age, rating and online status
    spy_age= 0
    spy_rating= 0.0
    spy_mode= False

#reading spy age
    spy_age= input("Tell me your age " +spy_name+ " :\n")

#spy age validation
    if(spy_age > 12 and spy_age < 50):

#read spy rating from user
        spy_rating= input("What's your spy rating:\n")

#ratings validations and messages
        if spy_rating > 4.5:
            print "Great! Ace"
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print "You're doing good soon to be an Ace\n"
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print "You can do better keep doing:"
        else:
            print "We can always use somebody to help in office!"

#make spy online
        spy_mode = True


#Authentication message
        print "Authentication Completed. Welcome '%s', Age: %s and rated: %s\n proud to have you onboard..."%(spy_name, spy_age, spy_rating)


#Error message for invalid age
    else:
        print "Oops! we regret to tell you " +spy_name+ " that your age is not appropriate to be a spy."

#error message for invalid name/ no name
else:
    print "A spy needs to have a valid name. Please try again..."