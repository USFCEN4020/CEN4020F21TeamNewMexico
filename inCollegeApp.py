import sqlite3

# connects or creates database, and a cursor for it
con = sqlite3.connect('inCollege.db')
cursor = con.cursor()

# Creates table if it was not built before
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (firstName, lastName, username, password, friend)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS skills
                (username, skills)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
                 (username, title, description, employer, location, salary)''')



# make this relatable to the friends
# cursor.execute('''CREATE TABLE IF NOT EXISTS friends
#                 (username)''')


# --------------------------GO TO PAGE---------------------------
# ****************************add to this list as we make new pages*********
def previous(pagesVisited):
    # pull up previous
    pagesVisited.pop()
    # last element in list
    print(pagesVisited[-1] + "\n")
    if pagesVisited[-1] == "mainpage":
        mainPage(pagesVisited)

    elif pagesVisited[-1] == "skills":
        skillsPage(pagesVisited)

    elif pagesVisited[-1] == " python":
        pythonPage(pagesVisited)

    elif pagesVisited[-1] == "java":
        javaPage(pagesVisited)

    elif pagesVisited[-1] == "c":
        cPage(pagesVisited)

    elif pagesVisited[-1] == "c++":
        cppPage(pagesVisited)

    elif pagesVisited[-1] == "ruby":
        rubyPage(pagesVisited)

    elif pagesVisited[-1] == "jobs":
        jobPage(pagesVisited)

    elif pagesVisited[-1] == "friends":
        friendsPage(pagesVisited)

    elif pagesVisited[-1] == "findfriends":
        findfriendsPage(pagesVisited)


# -----------------------SIGNUP------------------------------------


# ------------------------------------------------------------------
# Creates a new user in DB. Made it a separate function so it can be easily changed for future
def create_user(uName, passw, fName, lName):
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    tmpcursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, 0)", (fName, lName, uName, passw))
    print("succesfully registered")
    tmpcon.commit()
    tmpcon.close()


# True if username is found, false if not found
def check_for_username(uName): #tested
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM users WHERE username = ?", (uName,))
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcon.close()
        return True


# True if space, false if no space for users
def space_for_signup(): #tested
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute('SELECT * FROM users;')
    if len(curs.fetchall()) < 5:
        tmpcon.close()
        return True
    else:
        tmpcon.close()
        return False


# checks is password is correct
def is_good_password(pw): #tested
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


def signup(pagesVisited):
    # check for space
    if not space_for_signup():
        print("\nUser limit exceeded")
        # goTo homepage
        homepage()

    # enter input
    firstName = input("\nEnter first name: ")
    lastName = input("\nEnter last name: ")

    username = input("\nEnter Username: ")
    if check_for_username(username):
        print("Account with this username already exists!")
        signup(pagesVisited)    # added pagesVisited parameter here

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
    homepage()


# ---------------------------------LOGIN------------------------------------------------------------

# True if username and password for account is found, false if not found
def check_for_account(uName, password): #tested
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (uName, password))
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcon.close()
        return True


def login(pagesVisited):
    global username
    username = input("\nEnter Username: ")
    password = input("\nEnter Password: ")
    if check_for_account(username, password):
        # goToMainPage
        mainPage(pagesVisited)
    else:
        # allow user to ask to go back
        print("Invalid username or password. Please reenter!")
        login(pagesVisited)
        # goback option


# ---------------------------------MAINPAGE--------------------------------------------------------------

def print_options_menu():
    print("\n1. Job/Internship Search"
          "\n2. Find someone you know"
          "\n3. Learn a new skill"
          "\n4. Log Out")


def mainPage(pagesVisited):
    if not pagesVisited:
        pagesVisited.append("mainpage")
    elif pagesVisited[-1] != "mainpage":
        pagesVisited.append("mainpage")
    print_options_menu()
    selection = user_input(4)

    # added code
    sub_selection = None

    # goTo jobs
    if selection == 1:
        jobPage(pagesVisited)

    # goTo friends
    elif selection == 2:
        friendsPage(pagesVisited)

    # goTo skills
    elif selection == 3:
        skillsPage(pagesVisited)

    elif selection == 4:
        homepage()


# ---------------------------------SKILLS--------------------------------------------------------------

def print_skills_menu():
    print("\nSkills:"
          "\n1. Python"
          "\n2. Java"
          "\n3. C"
          "\n4. C++"
          "\n5. Ruby"
          "\n6. go Back")


def user_input(maxInput):
    my_selection = input("\nEnter your selection: ")
    # cast to int
    numSelection = int(my_selection)    # might cause casting error like if my_selection is alpha
    while not my_selection.isnumeric() or (numSelection > maxInput or numSelection < 1):
        my_selection = input("\nPlease enter a valid selection: ")
        numSelection = int(my_selection)

    return int(my_selection)


# FUNCTIONS TO IMPLEMENT LATER
def pythonPage(pagesVisited):
    if pagesVisited[-1] != "python":
        pagesVisited.append("python")
    print("\nThis page is currently under construction. Come back soon!")
    previous(pagesVisited)


def javaPage(pagesVisited):
    if pagesVisited[-1] != "java":
        pagesVisited.append("java")
    print("\nThis page is currently under construction. Come back soon!")
    previous(pagesVisited)


def cPage(pagesVisited):
    if pagesVisited[-1] != "c":
        pagesVisited.append("c")
    print("\nThis page is currently under construction. Come back soon!")
    previous(pagesVisited)


def cppPage(pagesVisited):
    if pagesVisited[-1] != "c++":
        pagesVisited.append("c++")
    print("\nThis page is currently under construction. Come back soon!")
    previous(pagesVisited)


def rubyPage(pagesVisited):
    if pagesVisited[-1] != "ruby":
        pagesVisited.append("ruby")
    print("\nThis page is currently under construction. Come back soon!")
    previous(pagesVisited)


def skillsPage(pagesVisited):
    if pagesVisited[-1] != "skills":
        pagesVisited.append("skills")
    print_skills_menu()
    selection = user_input(6)

    if selection == 1:
        pythonPage(pagesVisited)
    elif selection == 2:
        javaPage(pagesVisited)
    elif selection == 3:
        cPage(pagesVisited)
    elif selection == 4:
        cppPage(pagesVisited)
    elif selection == 5:
        rubyPage(pagesVisited)
    elif selection == 6:
        previous(pagesVisited)


# --------------------------------FRIENDS--------------------------------------

def friendsPage(pagesVisited):
    if pagesVisited[-1] != "friends":
        pagesVisited.append("friends")

        previous(pagesVisited)


# True if account is found with first and last name, false if not found
def find_friend_account(first, last): #tested
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM users WHERE firstName = '{}' AND lastName = '{}'".format(first, last))
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcon.close()
        return True

# ---------------------------------JOBS-------------------------------------------------------------


#   True if space, false if no space for jobs
def space_for_job(): #tested
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute('SELECT * FROM jobs;')
    if len(curs.fetchall()) < 5:
        tmpcon.close()
        return True
    else:
        tmpcon.close()
        return False



def jobPage(pagesVisited):
    if pagesVisited[-1] != "jobs":
        pagesVisited.append("jobs")
    print("\n1. Post a job"
          "\n2. Go back")

    selection = user_input(2)

    if selection == 1:
        my_title = input("\nJob title: ")
        my_description = input("\nJob description: ")
        my_employer = input("\nEmployer: ")
        my_location = input("\nJob location: ")
        my_salary = input("\nJob salary: ")
        post_job(my_title, my_description, my_employer, my_location, my_salary)
        jobPage(pagesVisited)
    elif selection == 2:
        previous(pagesVisited)


def post_job(my_title, my_description, my_employer, my_location, my_salary): #tested
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    previous_job_number = fetch_job_numbers() #track number if items in the table prior adding data
    if previous_job_number < 5:
        tmpcursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?)", (username, my_title, my_description, my_employer,
                                                                    my_location, my_salary))
    
    tmpcon.commit()
    # for testing purpose and validate that a job has been posted
    data = fetch_job_numbers() #track number if items in the table after adding data
    if data > previous_job_number: #comapring data 
        print("Job posted")
        tmpcon.close()
        return True
    else:
        print("job not posted")
        tmpcon.close()
        return False

def fetch_job_numbers(): #added function to return the number of items in the jobs table "tested"
    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    tmpcursor.execute("SELECT * FROM jobs")
    value = len(tmpcursor.fetchall())
    tmpcon.close()
    return value

# ------------------------------HOMEPAGE---------------------

def print_login_menu():
    print("\n1. Log In"
          "\n2. Sign Up"
          "\n3. Watch our video"
          "\n4. Search for a friend"
          "\n5. Exit")


def homepage():
    # when at the homepage menu, you shouldn't have access to prev
    pagesVisited = []
    username = ""
    password = ""
    selection = 0

    # Success story
    print("\nI was born with no money, no belly button, and five different father figures. "
          "Which father figure was the real one? I don't know. They all passed away before I could ask. "
          "During my time with inCollege has helped me find a job that has changed my life. "
          "I am now a full time janitor at google. "
          "With my impressive salary I have acquired a new belly button of my own, a life long dream. "
          "I have also successfully DNA tested myself to find out who my true father is. "
          "The results were interesting as my true father is Donald Trump. "
          "I am the true heir to the Trump fortune and now I am plotting my global takeover. "
          "Thank you inCollege, everything is thanks to your website.")

    print_login_menu()
    selection = user_input(5)

    # login option
    if selection == 1:  # log in
        login(pagesVisited)

    # signup option
    elif selection == 2:
        signup(pagesVisited)

    #   find friends option
    elif selection == 4:
        findfriendsPage(pagesVisited)

    # play video (not separate page)
    elif selection == 3:
        print("\nVideo now playing...")
        homepage()

    elif selection == 5:
        pass


# -------------------------FindFRIENDS---------------------------------------------------------------

def findfriendsPage(pagesVisited):
    pagesVisited.append("findfriends")
    print("\n1. Look for a friend"
          "\n2. Go back")

    selection = user_input(2)
    first = input("\nFirst name: ")
    last = input("\nLast name: ")

    if selection == 1:
        if find_friend_account(first, last):
            print("\nYour friend is on inCollege! Join them today."
                  "\n1. Log in"
                  "\n2. Sign up")

            selection = user_input(2)

            if selection == 1:
                login(pagesVisited)
            elif selection == 2:
                signup(pagesVisited)

        else:
            print("\nYour friend has not joined inCollege yet!")
            previous(pagesVisited)

    elif selection == 2:
        previous(pagesVisited)


# -------------------------EXECUTE---------------------------------------------------------------


homepage()

con.close()