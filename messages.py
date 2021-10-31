import database as db
import pages as page
import menus as menu
import prev_page as pv
import registration as reg


# ----------------------------------NOTE-----------------------------
# - add for example "page.pagesVisited[-1] != "inbox":
#                                   page.pagesVisited.append("inbox")" 
#   to every page you create with a menu, and add it to the previous page.
# - Add the parameters in the prev function as well. I forgot this easily
# - If you catch that I forgot to do that somewhere, please add it


def messagesPage(username):
    if page.pagesVisited[-1] != "messages":
        page.pagesVisited.append("messages")
    # print menu
    print("Welcome " + username + ". This is the messaging page \n")
    menu.printMessageOptions()
    selection = menu.user_input(2)

    if selection == 1:
        inbox()

    elif selection == 2:
        sendMessage(username)


def inboxNotification():
    inbox_list = db.cursor.execute("SELECT * FROM messages WHERE recipient = '{}'".format(reg.username)).fetchall()

    if len(inbox_list):
        return True
    else:
        return False


def inbox():
    if page.pagesVisited[-1] != "inbox":
        page.pagesVisited.append("inbox")

    #   list messages with 'recipient' of current user
    inbox_list = db.cursor.execute("SELECT * FROM messages WHERE recipient = '{}'".format(reg.username)).fetchall()

    if len(inbox_list) != 0:
        print("\nYour Inbox:")
        count = 1
        for i in inbox_list:
            print("\n{}. {}\t{}", count, inbox_list[0][1], inbox_list[0][2])
            count += 1

            #   user selection option to reply or delete
            print("\nSelect a message to reply or delete, or 0 to go back.")
            message_selection = menu.user_input(len(inbox_list))

            print("\n0. Go back\n1. Reply\n2. Delete")
            option_selection = menu.user_input(2)

            if option_selection == 1:
                #   sends reply to message_selection's sender
                print("Reply has been sent.")
                sendMessage(message_selection[0])
                page.mainPage()

            else:
                #   deletes message with message_selection's sender, recipient, and text
                inbox_list = db.cursor.execute(
                    "DELETE * FROM messages WHERE recipient = '{}' AND sender = '{}' AND text = '{}'",
                    message_selection[0], message_selection[1], message_selection[2])
                print("\nMessage has been deleted.")
                page.mainPage()

    #   if inbox empty
    else:
        print("\nYour inbox is empty, check again later!")
    page.mainPage()


def sendMessage(username):
    #   function to initialize sending message action
    if page.pagesVisited[-1] != "sendMessage":
        page.pagesVisited.append("sendMessage")

    sender = db.cursor.execute("SELECT * FROM users WHERE username = '{}'".format(reg.username)).fetchall()

    print("Would you like to send a message to a Friend or to Anyone?"
          "\nONLY plus members can select the Anyone option")
    menu.printSenderOptions()
    selection = menu.user_input(2)

    if selection == 1:
        sendToFriends()

    elif selection == 2:
        if sender[4] == 2:  # sender[plan] == 2 (Plus member)
            showEveryOne()
        else:
            print("\nSorry, Standard users can only send messages to their friends.")
            page.mainPage()


def sendToFriends():
    #   function to send message to friends (standard membership)
    if page.pagesVisited[-1] != "showFriends":
        page.pagesVisited.append("showFriends")

    print("Who would you like to send a Message to?")

    while True:
        result = db.cursor.execute(
            "SELECT status, friends_user FROM friends NATURAL JOIN users WHERE username = '{}'".format(
                reg.username)).fetchall()
        friends = db.cursor.execute(
            "SELECT * FROM friends WHERE status = 'accepted' and username = '{}'".format(reg.username)).fetchall()

        count = 1
        if len(friends) == 0:
            print("\nYou have no friends to send a message to")
            page.mainPage()

        else:
            print("Please select a friend")
            for i in result:
                if i[0] == "accepted":
                    name = db.cursor.execute("SELECT * FROM users WHERE username = '{}'".format(i[1])).fetchall()
                    print("{}. {} {}".format(count, name[0][0], name[0][1]))
                    count += 1

        print("\n\nEnter 0 to go back to main page.\n")

        selection = menu.user_input(len(friends))
        recipient = result[selection]

        #   should access name value of recipient (result[selection])
        createAMessage(recipient[0])



def showEveryOne():
    #   function to send message to anyone (plus membership)
    if page.pagesVisited[-1] != "showEveryOne":
        page.pagesVisited.append("showEveryOne")
    print("Who would you like to send a message to?")

    everyoneList = db.cursor.execute("SELECT * FROM users").fetchall()  # generate list of all users

    count = 1
    for i in everyoneList:
        print("{}. {}".format(count, everyoneList[0][0]))
        count += 1

    recipient = menu.user_input(len(everyoneList))

    createAMessage(recipient[0])  # should access name of selected recipient
    return


def createAMessage(recipient):
    # actual function to add message to messages table
    messageBody = input("\nEnter your message here: ")

    #   create entry in messages table
    #   sender = current user
    #   recipient = sendTo
    #   text = messageBody

    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    tmpcursor.execute("INSERT INTO messages VALUES (?, ?, ?, )", (reg.username, recipient, messageBody))

    pv.previous()

    return
