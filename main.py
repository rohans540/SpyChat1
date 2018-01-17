#importing default spy object
from spy_details import spy, friends
#import classes Spy and Chatmessage from spy_details
from spy_details import Spy,Chatmessage
from steganography.steganography import Steganography
from datetime import datetime
import csv

#=================================================load_friends method==================================================
#load_friends method used to load all the friends data from the friends.csv file

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)


        for row in reader:
            spy = Spy(name = row[0],salutation=row[1], age=int(row[2]), rating=float(row[3]))
            friends.append(spy)

#================================================SEND_MSG METHOD=======================================================
#send_msg method to send a secret message encoded in an image

def send_msg():

#selecting a friend to chat using select_a_friend method
    friend_choice = select_a_friend()

    original_img = raw_input('What is the name of the image:\n')

    output_path = 'output.jpg'

    txt = raw_input('Type your message here, don\'t worry it will be kept secret:\n')

#encoding the message in the image using encode method
    Steganography.encode(original_img, output_path, txt)

    sent_by_me = True

    newchat = Chatmessage(txt, sent_by_me)

    friends[friend_choice].chats.append(newchat)

    print "Your secret message is ready to be send\n"





#====================================================READ_MSG METHOD====================================================
#read_msg method to read a secret message encoded in an image by decoding it

def read_msg ():

#selecting a friend to read his message by calling select_a_friend method
    sender = select_a_friend()

    output_path = raw_input('What is the name of the file:\n')

#decoding the text encoded in the image using decode method
    secret_txt = Steganography.decode(output_path)

    sent_by_me = False

    newchat1 = Chatmessage(secret_txt, sent_by_me)

    friends[sender].chats.append(newchat1)

    print '\n\n'+secret_txt+'\n'

    print "Your secret message has been saved.\n"




#============================================START_CHAT METHOD=========================================================
#start_chat method: used to add chat functionality for the user

def start_chat(spy):

    current_status_msg = None
    spy.name = spy.salutation+" "+spy.name


    #age validation for spy
    if spy.age > 12 and spy.age < 40:

        print "Authentication complete.\nWelcome '%s', Age: %d with rating of %.1f. Proud to have you onboard"%(spy.name, spy.age, spy.rating)


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
                current_status_msg = add_status()
                print "Status Updated successfully\n"

            elif choice == '2':
                #add friend functionality
                number_of_friends = add_friend()

                print "You\'ve %d friends in your friendlist now\n"%(number_of_friends)

            elif choice == '3':
                #functionality to sending a secret message
                send_msg()


            elif choice == '4':
                #reading personal message
                read_msg()


            elif choice == '5':
                #reading chats from user
                print "check5\n"


            elif choice == '6':
                #exit from spychat
                print "Thank you for using spychat\nyou\'re logging out\n"
                spy.mode = False
                show_menu = False

            else:
                print "Ooops! The option you selected is not valid\nPlease try again"

    else:
        print "Ooops! you\'re age is not appropriate to be a spy\n"

#=================================================ADD_STATUS METHOD===================================================
#add_status method to set a new status message or to select an old one

def add_status():

    global STATUS_MSG
    if spy.current_status_msg != None:
        print "Your current status message is '%s'"%spy.current_status_msg
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
                msg_selection = int(msg_selection)
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
    newfriend = Spy('','', 0, 0.0)

    adding_more = True

    while adding_more:

        newfriend.name = raw_input("Please add your friend's name:\n")
        newfriend.salutation = raw_input("What should i call him/her Mr or Miss:\n")

        newfriend.name = newfriend.salutation+" "+newfriend.name

        newfriend.age = input('Enter your friend\'s age:\n')

        newfriend.rating = input('What\'s your friends spy rating:\n')




        #validation of a friend

        if len(newfriend.name) > 0 and newfriend.age > 12 and newfriend.age<=40 and newfriend.rating >= spy.rating and newfriend.name.isalpha():
            friends.append(newfriend)

            print "%s is added to your friend list as a new spy\n"%newfriend.name
            with open('friends.csv', 'a') as friend_details:
                writer = csv.writer(friend_details)
                writer.writerow([newfriend.name, newfriend.salutation, newfriend.age, newfriend.rating, newfriend.mode])


        else:
            #if friend is not eligible to be a spy

            print "Sorry! Your friend do not meet our criteria to be a your spy friend\n"

        while True:
                #to add more friends

            more = raw_input("Do you want to add more spy friends (Y/N)?\n")

            if more.upper() == 'N':
                adding_more = False
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
        print "\tPress %d for '%s'.\n"%(frno + 1, friend.name)
        frno = frno + 1

    while True:

        choice = input('Enter a choice from the above list:\n')

        if choice > len(friends):
            print "Invalid choice\please try again\n"
            continue
        else:

            frnd = friends[choice - 1]

        print "You selected your friend %s.\n"%(frnd.name)
        break

    return choice - 1


#======================================================MAIN BODY========================================================
#main started

STATUS_MSG = ['My name is bond, james bond', 'Shaken! not stirred.', 'Incredible India.']


print "Welcome to spychat\n Lets get started"


question = "Do you want to continue as %s %s say Y for yes or N for no:\n"%(spy.salutation, spy.name)

existing = raw_input(question)

if existing == 'Y' or existing == 'y':

    #load_friends method testing
    load_friends()

    #spychat menu if default spy comes to chat

    start_chat(spy)

elif existing == 'N' or existing == 'n':

    #if a new spy comes to chat, then save her details and redirect to spychat menu

    spy = Spy('', '', 0, 0.0,)

#reading spy name
    name = raw_input("Hey! Welcome to spychat\n You must tell me your name first:\n")

#name validation
    if len(name) > 0 and name.isalpha():

        print "Welcome '%s' Glad to have you back with us.\n"%(name)

        salutation = raw_input("What should i call you Mr or Miss:\n")

        print "Alright %s %s i would like to know a little bit more about you before we proceed..\n"%(salutation, name)

        age = input('Hey %s %s what is your Age?\n'%(salutation, name))


        if age > 12 and age < 40:


            rating = input("%s %s What is your spy rating?\n"%(salutation, name))

            if rating > 4.0 and rating < 5.0:
                print "Great! Ace\n"
            elif rating > 3.0 and rating < 4.0:
                print "Wow! Soon to be an Ace\n"
            else:
                print "You can always do better\n"

            spy = Spy(name, salutation, age, rating)
            start_chat(spy)

        else:
            print "Ooops! we regret to tell you %s %s that your age is not appropriate to be a spy\n"%(salutation, name)

    else:
        print "Ooops! you have entered an invalid name\nplease try again: "

else:
    print "Ooops! you have provided an invalid input\nplease try again\n"

