import registration as reg
import database as db
import pages as page
import menus as menu
import prev_page as pv

def friend_request(user1, user_sent):
    #just incase, users should be checked before entering
    if reg.check_for_username(user1) == False or reg.check_for_username(user_sent) == False:
        print("Username does not exist!")
        return

    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    #check if a friend request has been sent already
    curs = tmpcursor.execute("SELECT * FROM friends WHERE username = '{}' AND friends_user = '{}'".format(user1, user_sent))
    if str(curs.fetchone()) != "None":
        tmpcon.close()
        print("A friend request has already been sent to this user.")
        return

    #both friends will have friend
    tmpcursor.execute("INSERT INTO friends VALUES (?, ?, 'sent&pending')", (user1, user_sent))
    tmpcursor.execute("INSERT INTO friends VALUES (?, ?, 'pending')", (user_sent, user1)) 
    print("friend request sent")
    tmpcon.commit()
    tmpcon.close()


def friendsPage():
    if page.pagesVisited[-1] != "friends":
        page.pagesVisited.append("friends")
    search_type = None
    print("Student Search\n"+
          "Please select on of the following\n\n")
    
    print("1. Search by last name.\n" +
          "2. Search by major.\n" + 
          "3. Search by University\n" +
          "4. Go back\n\n")

    selection = menu.user_input(4)

    if int(selection) == 1:
        search_type = "lastName"
    elif int(selection) == 2:
        search_type = "major"
    elif int(selection) == 3:
        search_type = "university"
    elif int(selection) == 4:
        page.mainPage()
    
    search = input("Enter search value: ")

    if int(selection) != 1:
        result = db.cursor.execute("SELECT firstName, lastName, username FROM users NATURAL JOIN about where {} = '{}' COLLATE NOCASE".format(search_type, search)).fetchall()
    else:
        result = db.cursor.execute("SELECT firstName, lastName, username FROM users WHERE {} = '{}' COLLATE NOCASE".format(search_type, search)).fetchall()
    friendConnection  = None
    while (True):
        count = 1
        if len(result) == 0:
            print("No Student found with that entry.")
            friendsPage()
        else:
            for i in result:
                print("{}. {} {} {}".format(count, i[0], i[1], i[2]))
                count += 1
    
            print("\n\nEnter 0 to go back to search menu.\n")
            selection = input("Please enter the number of the user you would like to connect with: ")
            if int(selection) == 0:
                friendsPage()
            if int(selection) < 1 or int(selection) > len(result):
                continue
            else:
                friendConnection = result[int(selection) - 1][2]
                break
    friend_request(reg.username, friendConnection)
    page.mainPage()


# True if account is found with first and last name, false if not found
def find_friend_account(first, last):  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM users WHERE firstName = '{}' AND lastName = '{}'".format(first, last))
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcon.close()
        return True

#adds friends
#user1 sends it to user2

def findfriendsPage():
    page.pagesVisited.append("findfriends")
    print("\n1. Look for a friend"
          "\n2. Go back")

    selection = menu.user_input(2)

    if selection == 1:
        first = input("\nFirst name: ")
        last = input("\nLast name: ")
        if find_friend_account(first, last):
            print("\nYour friend is on inCollege! Join them today."
                  "\n1. Log in"
                  "\n2. Sign up")

            selection = menu.user_input(2)

            if selection == 1:
                reg.login()
            elif selection == 2:
                reg.signup()

        else:
            print("\nYour friend has not joined inCollege yet!")
            pv.previous()

    elif selection == 2:
        pv.previous()



#----------------PENDING_--------------------

#false if no pending friend requests
def pending_friend(username):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM friends WHERE username = '{}' AND status = 'pending'".format(username))
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcon.close()
        return True


def view_pending_requests():
    if page.pagesVisited[-1] != "view pending requests":
        page.pagesVisited.append("view pending requests")
    while (True):
        result = db.cursor.execute("SELECT status, friends_user FROM friends NATURAL JOIN users WHERE username = '{}'".format(reg.username)).fetchall()
        pending = db.cursor.execute("SELECT * FROM friends WHERE status = 'pending' and username = '{}'".format(reg.username)).fetchall()
        
        count = 1
        if len(pending) == 0 :
            print("\nNo requests pending")
            page.mainPage()
        else:
            for i in result:
                
                if i[0] == "pending":
                    name = db.cursor.execute("SELECT * FROM users WHERE username = '{}'".format(i[1])).fetchall()
                    print("{}. {} {} has sent you a friend request.".format(count, name[0][0], name[0][1]))
                    
                    count += 1

        print("\n\nEnter 0 to go back to main page.\n")

        selection = menu.user_input(len(pending))

        db.cursor.execute("UPDATE friends SET status = 'accepted' WHERE username = '{}'".format(result[(selection) - 1][1]))
        db.cursor.execute("UPDATE friends SET status = 'accepted' WHERE username = '{}'".format(reg.username))
        db.con.commit()
        view_pending_requests()




        
      
    