import registration as reg
import database as db
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