import database as db
import pages as page

# -----------------------SIGNUP------------------------------------

# Creates a new user in DB. Made it a separate function so it can be easily changed for future
def create_user(uName, passw, fName, lName):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    tmpcursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, 0)", (fName, lName, uName, passw))
    tmpcursor.execute("INSERT INTO settings VALUES (?, ?, ?, ?, ?)", (uName, "ON", "ON", "ON", "English"))
    print("succesfully registered")
    tmpcon.commit()
    tmpcon.close()


# True if username is found, false if not found
def check_for_username(uName):  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM users WHERE username = ?", (uName,))
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcon.close()
        return True


# True if space, false if no space for users
def space_for_signup():  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute('SELECT * FROM users;')
    if len(curs.fetchall()) < 5:
        tmpcon.close()
        return True
    else:
        tmpcon.close()
        return False


# checks is password is correct
def is_good_password(pw):  # tested
    has_capital = False
    has_number = False
    has_non_alphanum = False

    if len(pw) < 8 or len(pw) > 12:
        return False

    for char in pw:
        if char.isnumeric():
            has_number = True
        if not (char.isalnum()):
            has_non_alphanum = True
        if char.isupper():
            has_capital = True

    if has_number and has_capital and has_non_alphanum:
        return True
    else:
        return False


def signup():
    # check for space
    if not space_for_signup():
        print("\nUser limit exceeded")
        # goTo homepage
        page.homepage()

    print("Default settings:\nInCollege Email -> ON"
          "\nSMS -> ON"
          "\nTargeted Advertising -> ON"
          "\nLanguage -> English"
          "\n If you wish to change it, please log in and modify in privacy Policy")

    # enter input
    firstName = input("\n\nEnter first name: ")
    lastName = input("\nEnter last name: ")

    username = input("\nEnter Username: ")
    if check_for_username(username):
        print("Account with this username already exists!")
        signup()  # added pagesVisited parameter here

    password = input("\nEnter Password: ")
    if is_good_password(password):
        create_user(username, password, firstName, lastName)
    else:
        while not is_good_password(password):
            password = input("\nPassword must contain each of the following: "
                             "\nan uppercase letter, a non-alphanumeric character, and a number."
                             "\nPlease re-enter: ")
        create_user(username, password, firstName, lastName)
    # goTo homepage
    page.homepage()


# ---------------------------------LOGIN------------------------------------------------------------

# True if username and password for account is found, false if not found
def check_for_account(uName, password):  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (uName, password))
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcon.close()
        return True


def login():
    global username
    
    # set the flag of log in to true
    username = input("\nEnter Username: ")
    password = input("\nEnter Password: ")
    if check_for_account(username, password):
        # goToMainPage
        page.mainPage()
    else:
        # allow user to ask to go back
        print("Invalid username or password. Please reenter!")
        login()
        # goback option
    
