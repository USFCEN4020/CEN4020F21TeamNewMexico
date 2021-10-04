
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

