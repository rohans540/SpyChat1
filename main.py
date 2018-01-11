#importing necessary variables from the file name spy_details
from spy_details import spy
from steganography.steganography import Steganography
#============================================SPY_CHAT METHOD=========================================================
#start_chat method: used to add chat functionality for the user

def start_chat(spy):

    current_status_msg = None
    spy['name'] = spy['salutation']+" "+spy['name']


    #age validation for spy
    if spy['age'] > 12 and spy['age'] < 40:

        print "Authentication complete.\nWelcome '%s', Age: %d with rating of %.1f. Proud to have you onboard"%(spy['name'], spy['age'], spy['rating'])


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
                print "check3\n"


            elif choice == '4':
                #reading personal message
                print "check4\n"


            elif choice == '5':
                #reading chats from user
                print "check5\n"


            elif choice == '6':
                #exit from spychat
                print "Thank you for using spychat\noyou\'re logging out\n"
                spy_mode = False
                show_menu = False

            else:
                print "Ooops! The option you selected is not valid\nPlease try again"

    else:
        print "Ooops! you\'re age is not appropriate to be a spy\n"

#=================================================ADD_STATUS METHOD===================================================
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

#=========================================================ADD_FRIEND METHOD============================================
#add_friend Method definition input:None, output:a new friend added

def add_friend():


    #use of dictionary to store details of a new friend
    newfriend = {
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0
    }

    newfriend['name'] = raw_input("Please add your friend's name:\n")
    newfriend['salutation'] = raw_input("What should i call him/her Mr or Miss:\n")

    newfriend['name'] = newfriend['salutation']+" "+newfriend['name']

    newfriend['age'] = input('Enter your friend\'s age:\n')

    newfriend['rating'] = input('What\'s your friends spy rating:\n')




        #validation of a friend

    if len(newfriend['name']) > 0 and newfriend['age'] > 12 and newfriend['age'] < 40 and newfriend['rating'] >= spy['rating'] and newfriend['name'].isalpha():
        friends.append(newfriend)

        print "%s is added to your friend list as a new spy\n"%(newfriend['name'])

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

    return len(friends)

#=================================================SELECT_A_FRIEND METHOD================================================

#Method select_a_friend to select a friend from friends list to chat

def select_a_friend():

    frno = 0

    print "Choose a friend from the list.\n"

    for friend in friends:
        print "\tPress %d for '%s'.\n"%(frno + 1, friend['name'])
        frno = frno + 1

    while True:

        choice = input('Enter a choice from the above list:\n')

        if int(choice) > len(friends):
            print "Invalid choice\please try again\n"
            continue
        else:

            frnd = friends[choice - 1]

        print "You selected your friend %s.\n"%(frnd['name'])

        return choice - 1


#======================================================MAIN BODY========================================================
#main started

STATUS_MSG = ['My name is bond, james bond', 'Shaken! not stirred.', 'Incredible India.']

friends = []


print "Welcome to spychat\n Lets get started"


question = raw_input("Do you want to continue as %s %s say Y for yes or N for no:\n"%(spy['salutation'], spy['name']))

existing = raw_input(question)

if existing.upper() == 'Y':

    #spychat menu if default spy comes to chat

    start_chat(spy)

elif existing.upper() == 'N':

    #if a new spy comes to chat, then save her details and redirect to spychat menu

    spy = {
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0,
        'mode': False
    }

#reading spy name
    spy['name'] = raw_input("Hey! Welcome to spychat\n You must tell me your name first:\n")

#name validation
    if len(spy['name']) > 0 and spy['name'].isalpha():

        print "Welcome '%s' Glad to have you back with us.\n"%(spy['name'])

        spy['salutation'] = raw_input("What should i call you Mr or Miss:\n")

#concatenating salutation and name
        spy['name'] = spy['salutation']+" "+spy['name']

        print "Alright %s i would like to know a little bit more about you before we proceed..\n"%(spy['name'])

        spy['age'] = input('Hey %s what is your Age?\n'%(spy['name']))

        spy['age'] = int(spy['age'])

        if spy['age'] > 12 and spy['age'] < 40:


            spy['rating'] = input("%s What is your spy rating?\n"%(spy['name']))

            if spy['rating'] > 4.0 and spy['rating'] < 5.0:
                print "Great! Ace\n"
            elif spy['rating'] > 3.0 and spy['rating'] < 4.0:
                print "Wow! Soon to be an Ace\n"
            else:
                print "You can always do better\n"
        else:
            print "Ooops! we regret to tell you %s that your age is not appropriate to be a spy\n"%(spy['name'])

    else:
        print "Ooops! you have entered an anvalid name\nplease try again: "

else:
    print "Ooops! you have provided an invalid input\nplease try again\n"

