#importing necessary variables from the file name spy_details
from spy_details import spy_name, spy_salutation, spy_age, spy_rating, spy_mode

#start_chat method: used to add chat functionality for the user

def start_chat(spy_name, spy_age, spy_rating):

    global spy_mode

    current_status_msg = None
    spy_name = spy_salutation+" "+spy_name


    #age validation for spy
    if spy_age > 12 and spy_age < 40:

        print "Authentication complete.\nWelcome '%s', Age: %d with rating of %.1f. Proud to have you onboard"%(spy_name, spy_age, spy_rating)


        #loop to keep the menu
        show_menu = True
        while show_menu:
            print"""
            Select an option of you choice:
                    1. Update status
                    2. Add a friend
                    3. Send a secret message
                    4. Read a personal message
                    5. Read chats from user
                    6. Exit to home"""
            choice = raw_input()

            if choice == '1':
                current_status_msg = add_status(current_status_msg)
                print "Status Updated successfully\n"

            elif choice == '2':
                #add friend functionality
                number_of_friends = add_friend()

                print "You\'ve %d friends in your friendlist now\n"%(number_of_friends)

            elif choice == '3':
                #functionality to sending a secret message

            elif choice == '4':
                #reading personal message

            elif choice == '5':
                #reading chats from user

            elif choice == '6':
                #exit from spychat
                print "Thank you for using spychat\noyou\'re logging out\n"
                spy_mode = False
                show_menu = False

            else:
                print "Ooops! The option you selected is not valid\nPlease try again"

    else:
        print "Ooops! you\'re age is not appropriate to be a spy\n"


#add_status method to set a new status message or to select an old one

def add_status(current_status_msg):
    global STATUS_MSG

    if current_status_msg != None:
        print "Your current status message is '%s'"%current_status_msg
    else:
        print "You don\'t have any status message currently\n"

    while True:

        default = raw_input("Do you want to select one from the older statuses (Y/N)?\n")

        #if spy want to set a new status
        if default.upper() == 'N':
            new_status_msg = raw_input("Alright! Type your status:\n")

            if len(new_status_msg) > 0:
                updated_status_msg = new_status_msg
                STATUS_MSG.append(updated_status_msg)
                break

            else:
                print "You have not written anything\nplease try again\n"

        #if spy want to select an older status
        elif default.upper() == 'Y':
            item_position = 1

            #if there is no older status in the buffer
            if STATUS_MSG == []:
                print "sorry! you do not have any older status messages\nSelect 'N for creating a new one\n'"

                continue

            #showing list of older status
            for msg in STATUS_MSG:
                print "%d. %s\n"%(item_position, msg)
                item_position = item_position + 1

            while True:

                msg_selection = raw_input("Choose from the above messages:\n")
                if len(STATUS_MSG) >= msg_selection:
                    updated_status_msg = STATUS_MSG[msg_selection - 1]
                    break

                #if spy choose an exceeding number
                else:
                    print "You\'ve selected an invalid option\nPlease Try again\n"

            break

        else:
            print "You've entered an invalid key\nplease try again\n"

    return updated_status_msg


#add_friend Method definition input:None, output:a new friend added

def add_friend():

    global friends_name, friends_age, friends_rating, friends_mode, spy_rating

    newfriend = True

    while newfriend:


        #details of spy friend

        new_name = raw_input("Enter you friend's name:\n")
        new_salutation = raw_input("What should we call your friend Mr. or Miss?\n")
        new_name = new_salutation+" "+new_name
        new_age = input("Enter your friend's age:\n")
        new_rating = input("Enter your friend's rating:\n")


        #validation of a friend

        if len(new_name) > 0 and new_age > 12 and new_age < 40 and new_rating >= spy_rating and new_name.isalpha():
            friends_name.append(new_name)
            friends_age.append(new_age)
            friends_rating.append(new_rating)
            friends_mode.append(True)
            print "%s is added to your friend list as a new spy\n"%(new_name)

        else:
            #if friend is not eligible to be a spy

            print "Sorry! Your friend do not meet our criteria to be a your spy friend\n"

        while True:
            #to add more friends

            more = raw_input("Do you want to add more spy friends (Y/N)?\n")

            if more.upper() == 'N':
                newfriend = False
                break

            elif more.upper() == 'Y':

                break

            else:
                print "Press a valid key Y or N\n"

    return len(friends_name)

#main started

STATUS_MSG = ['My name is bond, james bond', 'Shaken! not stirred.', 'Incredible India.']

friends_name = []
friends_age = []
friends_rating = []
friends_mode = []


print "Welcome to spychat\n Lets get started"


question = raw_input("Do you want to continue as %s %s say Y for yes or N for no:\n"%spy_salutation, spy_name)

existing = raw_input(question)

if existing.upper() == 'Y':

    #spychat menu if default spy comes to chat

    start_chat(spy_name, spy_age, spy_rating)

elif existing.upper() == 'N':

    #if a new spy comes to chat, then save her details and redirect to spychat menu

    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_mode = False

#reading spy name
    spy_name = raw_input("Hey! Welcome to spychat\n You must tell me your name first:\n")

#name validation
    if len(spy_name) > 0 and spy_name.isalpha():

        print "Welcome '%s' Glad to have you back with us.\n"%(spy_name)

        spy_salutation = raw_input("What should i call you Mr or Miss:\n")

#concatenating salutation and name
        spy_name = spy_salutation+" "+spy_name

        print "Alright %s i would like to know a little bit more about you before we proceed..\n"%(spy_name)

        spy_age = input('Hey %s what is your Age?\n'%(spy_age))

        spy_age = int(spy_age)

        if spy_age > 12 and spy_age < 40:


            spy_rating = input("%s What is your spy rating?\n"%(spy_name))

            if spy_rating > 4.0 and spy_rating < 5.0:
                print "Great! Ace\n"
            elif spy_rating > 3.0 and spy_rating < 4.0:
                print "Wow! Soon to be an Ace\n"
            else:
                print "You can always do better\n"
        else:
            print "Ooops! we regret to tell yo %s that your age is not appropriate to be a spy\n"

    else:
        print "Ooops! you have entered an anvalid name\nplease try again: "

    else:
        print "Ooops! you have provided an invalid input\nplease try again\n"

