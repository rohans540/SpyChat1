#importing default spy object
from spy_details import spy, friends
#import classes Spy and Chatmessage from spy_details
from spy_details import Spy,Chatmessage
#importing steganography library to use its services
from steganography.steganography import Steganography
from datetime import datetime
import csv
from termcolor import colored
from colorama import init


#=================================================load_friends method==================================================
#load_friends method used to load all the friends data from the friends.csv file

def load_friends():
    with open('friends.csv', 'rb') as friends_data:     #opening file friends.csv in read mode
        reader = csv.reader(friends_data)

        print colored("Your friends are:\t\n", "blue")


        for row in reader:
            spy = Spy(name = row[0],salutation=row[1], age=int(row[2]), rating=float(row[3]))
            friends.append(spy)
            print colored(row, "magenta")       #print all friends from the friends.csv file

#================================================SEND_MSG METHOD=======================================================
#send_msg method to send a secret message encoded in an image

def send_msg():

#selecting a friend to chat using select_a_friend method
    friend_choice = select_a_friend()

    original_img = raw_input(colored('What is the name of the image:\n', "blue"))   #reading the pathname of orginal image

    output_path = 'output.jpg'      #specifying the pathname of output image

    txt = raw_input(colored('Type your message here, don\'t worry it will be kept secret:\n', "blue")) #reading secret message

#encoding the message in the image using encode method
    Steganography.encode(original_img, output_path, txt)

    sent_by_me = True

    newchat = Chatmessage(txt, sent_by_me)

    friends[friend_choice].chats.append(newchat)

    print colored("Your secret message is ready to be send\n", 'blue')

#==================================================SEND_HELP_MESSAGE====================================================

def send_help_msg():

#selecting the friend
    friend_choice = select_a_friend()

#the text response
    txt = "Don't panic I am on my way to reach you!"

#creating new chat
    newchat = Chatmessage(colored(txt,'red'), True)

#appending the chat
    friends[friend_choice].chats.append(newchat)





#====================================================READ_MSG METHOD====================================================
#read_msg method to read a secret message encoded in an image by decoding it

def read_msg ():

#selecting a friend to read his message by calling select_a_friend method
    sender = select_a_friend()

    output_path = raw_input(colored('What is the name of the file you want to decode:\n', "blue"))


    try:
#decoding the text encoded in the image using decode method
        secret_txt = Steganography.decode(output_path)
        print colored("The secret message is:\n\t", 'blue')
        print colored(secret_txt,'magenta')

    #converting the secret_txt to uppercase
        new = (secret_txt.upper()).split()

#checking emergency templates for help
        if "SOS" in new or "SAVE" in new or "HELP" in new or "ACCIDENT" in new or "RESCUE" in new or "ALERT" in new:

            print colored("!", 'grey', 'on_yellow'),
            print colored("!", 'grey', 'on_yellow'),
            print colored("!", 'grey', 'on_yellow')


            print colored("Your friend the sender of this message need an emergency", 'green')
            print colored("Please help your friend by sending him a helping message.\n", 'green')
            print colored("Select that friend to send him a helping message.\n", 'green')

#calling send_help_msg() to send the help
            send_help_msg()

            print colored("You have sent a message to help your friend", 'green')

#creating new chat
            new_chat = Chatmessage(secret_txt, False)
#appending to chats
            friends[sender].chats.append(new_chat)

#if there is no emergency messages or call for help
        else:
            new_chat = Chatmessage(secret_txt, False)
            friends[sender].chats.append(new_chat)
            print colored("Your secret message has been saved.\n", 'green')

#no message found exception
    except TypeError:
        print colored("Nothing to decode from the image\nsorry! there is no secret message", 'red')



#====================================================READ_CHATS METHOD===================================================
#read_chats method to read the chat history from friends

def read_chats():

    read_from = select_a_friend()

    print "\n"

    for chat in friends[read_from].chats:
        if chat.sent_by_me:
            print colored(str(chat.time.strftime("%d %B %Y %A %H: %M"))+',',"blue")

            print colored("You:","green")

            print str(chat.message)

        else:
            print colored(str(chat.time.strftime("%d %B %Y %A %H: %M", "blue")))

            print colored(str(friends[read_from].name)+"he:", "red")

            print str(chat.message)





#============================================START_CHAT METHOD=========================================================
#start_chat method: used to add chat functionality for the user

def start_chat(spy):

    current_status_msg = None
    spy.name = spy.salutation+" "+spy.name


    #age validation for spy
    if spy.age > 12 and spy.age < 40:

        print colored("Authentication complete.\nWelcome '%s', Age: %d with rating of %.1f. Proud to have you onboard", "green")%(spy.name, spy.age, spy.rating)


        #loop to keep the menu
        show_menu = True
        while show_menu:
            print colored("""
            Select an option of you choice:
                    1. Update status
                    2. Add a friend
                    3. Send a secret message
                    4. Read a personal message
                    5. Read chats from user
                    6. Exit to home""", "magenta")
            choice = raw_input()

            if choice == '1':
                current_status_msg = add_status()
                print colored("Status Updated successfully\n", "green")

            elif choice == '2':
                #add friend functionality
                number_of_friends = add_friend()

                print colored("You\'ve %d friends in your friendlist now\n", "green")%(number_of_friends)

            elif choice == '3':
                #functionality to sending a secret message
                send_msg()


            elif choice == '4':
                #reading personal message
                read_msg()


            elif choice == '5':
                #reading chats from user
                read_chats()


            elif choice == '6':
                #exit from spychat
                print colored("Thank you for using spychat\nyou\'re logging out\n", "green")
                spy.mode = False
                show_menu = False

            else:
                print colored("Ooops! The option you selected is not valid\nPlease try again", "red")

    else:
        print colored("Ooops! you\'re age is not appropriate to be a spy\n", "red")

#=================================================ADD_STATUS METHOD===================================================
#add_status method to set a new status message or to select an old one

def add_status():

    global STATUS_MSG
    if spy.current_status_msg != None:
        print colored("Your current status message is '%s'", "green")%spy.current_status_msg
    else:
        print colored("You don\'t have any status message currently\n", "red")

    while True:

        default = raw_input(colored("Do you want to select one from the older statuses (Y/N)?\n", "blue"))

        #if spy want to set a new status
        if default.upper() == 'N':
            new_status_msg = raw_input(colored("Alright! Type your status:\n", "cyan"))

            if len(new_status_msg) > 0:
                updated_status_msg = new_status_msg
                STATUS_MSG.append(updated_status_msg)
                break

            else:
                print colored("You have not written anything\nplease try again\n", "red")

        #if spy want to select an older status
        elif default.upper() == 'Y':
            item_position = 1

            #if there is no older status in the buffer
            if STATUS_MSG == []:
                print colored("sorry! you do not have any older status messages\nSelect 'N for creating a new one\n'", "red")

                continue

            #showing list of older status
            for msg in STATUS_MSG:
                print colored("%d. %s\n", "magenta")%(item_position, msg)
                item_position = item_position + 1

            while True:

                msg_selection = raw_input(colored("Choose from the above messages:\n", "blue"))
                msg_selection = int(msg_selection)
                if len(STATUS_MSG) >= msg_selection:
                    updated_status_msg = STATUS_MSG[msg_selection - 1]
                    break

                #if spy choose an exceeding number
                else:
                    print colored("You\'ve selected an invalid option\nPlease Try again\n", "red")

            break

        else:
            print colored("You've entered an invalid key\nplease try again\n", "red")

    return updated_status_msg

#=========================================================ADD_FRIEND METHOD============================================
#add_friend Method definition input:None, output:a new friend added

def add_friend():


    #use of dictionary to store details of a new friend
    newfriend = Spy('','', 0, 0.0)

    adding_more = True

    while adding_more:

        newfriend.name = raw_input(colored("Please add your friend's name:\n", "blue"))
        newfriend.salutation = raw_input(colored("What should i call him/her Mr or Miss:\n", "blue"))

        newfriend.age = input(colored('Enter your friend\'s age:\n', "blue"))

        newfriend.rating = input(colored('What\'s your friends spy rating:\n', "blue"))
        newfriend.rating = float(newfriend.rating)




        #validation of the friend

        if len(newfriend.name) > 0 and 12 < newfriend.age < 40 and newfriend.rating >= spy.rating and newfriend.name.isalpha()==False:
            friends.append(newfriend)

            print colored("%s %s is added to your friend list as a new spy\n", "green")%newfriend.salutation,newfriend.name

#writing the friends details to file friends.csv
            with open('friends.csv', 'a') as friend_details:    #opening the file in append mode
                writer = csv.writer(friend_details)
                writer.writerow([newfriend.name, newfriend.salutation, newfriend.age, newfriend.rating, newfriend.mode])


        else:
            #if friend is not eligible to be a spy

            print colored("Sorry! Your friend do not meet our criteria to be a your spy friend\n", "red")

        while True:
                #to add more friends

            more = raw_input(colored("Do you want to add more spy friends (Y/N)?\n", "blue"))

            if more.upper() == 'N':
                adding_more = False
                break

            elif more.upper() == 'Y':

                break

            else:
                print colored("Press a valid key Y or N\n", "red")

    return len(friends)

#=================================================SELECT_A_FRIEND METHOD================================================

#Method select_a_friend to select a friend from friends list to chat

def select_a_friend():

    frno = 0

    print colored("Choose a friend from the list.\n", "blue")

    for friend in friends:
        print colored("\tPress %d for '%s'.\n", "magenta")%(frno + 1, friend.name)
        frno = frno + 1

    while True:

        choice = input(colored('Enter a choice from the above list:\n', "blue"))

        if choice > len(friends):
            print colored("Invalid choice\please try again\n", "red")
            continue
        else:

            frnd = friends[choice - 1]

        print colored("You selected your friend %s.\n", "green")%(frnd.name)
        break

    return choice - 1


#======================================================MAIN BODY========================================================
#main started

STATUS_MSG = ['My name is bond, james bond', 'Shaken! not stirred.', 'Incredible India.']


print colored("Welcome to spychat\n Lets get started", "green")


question = colored("Do you want to continue as %s %s say Y for yes or N for no:\n", "blue")%(spy.salutation, spy.name)

existing = raw_input(colored(question, "blue"))

if existing == 'Y' or existing == 'y':

    #load_friends method testing
    load_friends()

    #spychat menu if default spy comes to chat

    start_chat(spy)

elif existing == 'N' or existing == 'n':

    #if a new spy comes to chat, then save her details and redirect to spychat menu

    spy = Spy('', '', 0, 0.0,)

#reading spy name
    name = raw_input(colored("Hey! Welcome to spychat\n You must tell me your name first:\n", "blue"))
#name validation
    if len(name) > 0 and name.isalpha():

        print colored("Welcome '%s' Glad to have you back with us.\n", "green")%(name)

        salutation = raw_input(colored("What should i call you Mr or Miss:\n", "blue"))

        print colored("Alright %s %s i would like to know a little bit more about you before we proceed..\n", "green")%(salutation, name)

        age = input(colored('Hey %s %s what is your Age?\n', "blue")%(salutation, name))


        if age > 12 and age < 40:


            rating = input(colored("%s %s What is your spy rating?\n", "blue")%(salutation, name))

            if rating > 4.0 and rating < 5.0:
                print colored("Great! Ace\n", "green")
            elif rating > 3.0 and rating < 4.0:
                print colored("Wow! Soon to be an Ace\n", "blue")
            else:
                print colored("You can always do better\n", "red")

            spy = Spy(name, salutation, age, rating)
            start_chat(spy)

        else:
            print colored("Ooops! we regret to tell you %s %s that your age is not appropriate to be a spy\n", "red")%(salutation, name)

    else:
        print colored("Ooops! you have entered an invalid name\nplease try again: ", "red")

else:
    print colored("Ooops! you have provided an invalid input\nplease try again\n", "red")

