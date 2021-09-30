#NOTE

# 1) make sure to seperate EVERY individual page in a different function
# 2) Add the new page created to the previous() with the according string and function
# 3) also DONT FORGOT to append the page to the vistedPages list
# 4) make sure you change the paramater of user_input() when the size of the menu changes

#changes
#added job_post_function
#made pagesVisited list global. Now it doesn't need to be passed through every's page paramater anymore

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


def previous():
    # pull up previous
    pagesVisited.pop()
    # last element in list
    print(pagesVisited[-1] + "\n")

    if pagesVisited[-1] == "homepage":
        homepage()

    if pagesVisited[-1] == "mainpage":
        mainPage()

    elif pagesVisited[-1] == "skills":
        skillsPage()

    elif pagesVisited[-1] == "python":
        pythonPage()

    elif pagesVisited[-1] == "java":
        javaPage()

    elif pagesVisited[-1] == "c":
        cPage()

    elif pagesVisited[-1] == "c++":
        cppPage()

    elif pagesVisited[-1] == "ruby":
        rubyPage()

    elif pagesVisited[-1] == "jobs":
        jobPage()
    
    elif pagesVisited[-1] == "post a job":
        post_job_page()

    elif pagesVisited[-1] == "friends":
        friendsPage()

    elif pagesVisited[-1] == "findfriends":
        findfriendsPage()

    elif pagesVisited[-1] == "useful links":
        usefulLinksPage()
    
    elif pagesVisited[-1] == "important links":
        importantLinksPage()

    elif pagesVisited[-1] == "general":
        generalPage()

    elif pagesVisited[-1] == "browse in college":
        browseInCollegePage()

    elif pagesVisited[-1] == "business solutions":
        businessSolutionsPage()

    elif pagesVisited[-1] == "directories":
        directories()

    elif pagesVisited[-1] == "copyright notice":
        copyrightNotice()
    
    elif pagesVisited[-1] == "about":
        about()
      
    elif pagesVisited[-1] == "accessibility":
        accessibility()
     
    elif pagesVisited[-1] == "user agreement":
        userAgreement()

    elif pagesVisited[-1] == "privacy policy":
        privacyPolicy()

    elif pagesVisited[-1] == "cookie policy":
        cookiePolicy()

    elif pagesVisited[-1] == "copyright policy":
        copyRightPolicy()

    elif pagesVisited[-1] == "brand policy":
        brandPolicy()
    
    elif pagesVisited[-1] == "guest controls":
        guestControls()
     
    elif pagesVisited[-1] == "languages":
        languages()
     
    elif pagesVisited[-1] == "":
        return


# -----------------------SIGNUP------------------------------------

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


def signup():
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
        signup()    # added pagesVisited parameter here

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


def login():
    global username
    username = input("\nEnter Username: ")
    password = input("\nEnter Password: ")
    if check_for_account(username, password):
        # goToMainPage
        mainPage()
    else:
        # allow user to ask to go back
        print("Invalid username or password. Please reenter!")
        login()
        # goback option


# ---------------------------------MAINPAGE--------------------------------------------------------------

def print_options_menu():
    print("\n1. Job/Internship Search"
          "\n2. Find someone you know"
          "\n3. Learn a new skill"
          "\n4. Log Out")


def mainPage():
    if not pagesVisited:
        pagesVisited.append("mainpage")
    elif pagesVisited[-1] != "mainpage":
        pagesVisited.append("mainpage")
    print_options_menu()
    selection = user_input(6)

    # added code
    sub_selection = None

    # goTo jobs
    if selection == 1:
        jobPage()

    # goTo friends
    elif selection == 2:
        friendsPage()

    # goTo skills
    elif selection == 3:
        skillsPage()

    elif selection == 4:
        usefulLinksPage()

    elif selection == 5:
        importantLinksPage()

    elif selection == 5:
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
def pythonPage():
    if pagesVisited[-1] != "python":
        pagesVisited.append("python")
    print("\nThis page is currently under construction. Come back soon!")
    previous()


def javaPage():
    if pagesVisited[-1] != "java":
        pagesVisited.append("java")
    print("\nThis page is currently under construction. Come back soon!")
    previous()


def cPage():
    if pagesVisited[-1] != "c":
        pagesVisited.append("c")
    print("\nThis page is currently under construction. Come back soon!")
    previous()


def cppPage():
    if pagesVisited[-1] != "c++":
        pagesVisited.append("c++")
    print("\nThis page is currently under construction. Come back soon!")
    previous()


def rubyPage():
    if pagesVisited[-1] != "ruby":
        pagesVisited.append("ruby")
    print("\nThis page is currently under construction. Come back soon!")
    previous()


def skillsPage():
    if pagesVisited[-1] != "skills":
        pagesVisited.append("skills")
    print_skills_menu()
    selection = user_input(6)

    if selection == 1:
        pythonPage()
    elif selection == 2:
        javaPage()
    elif selection == 3:
        cPage()
    elif selection == 4:
        cppPage()
    elif selection == 5:
        rubyPage()
    elif selection == 6:
        previous()


# --------------------------------FRIENDS--------------------------------------

def friendsPage():
    if pagesVisited[-1] != "friends":
        pagesVisited.append("friends")

        previous()


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

def jobPage():
    if pagesVisited[-1] != "jobs":
        pagesVisited.append("jobs")
    print("\n1. Post a job"
          "\n2. Go back")

    selection = user_input(2)

    if selection == 1:
        post_job_page()

    elif selection == 2:
        previous()


def post_job_page():
    my_title = input("\nJob title: ")
    my_description = input("\nJob description: ")
    my_employer = input("\nEmployer: ")
    my_location = input("\nJob location: ")
    my_salary = input("\nJob salary: ")
    post_job(my_title, my_description, my_employer, my_location, my_salary)
    jobPage()


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
          "\n3. Watch Our Video"
          "\n4. Search for a Friend"
          "\n5. Useful Links"
          "\n6. Imoportant Links"
          "\n7. Exit")

    #****NOTE*******
    #Change this number when we add options
    optionNum = 7
    return optionNum
    

def homepage():
    # when at the homepage menu, you shouldn't have access to prev
    global pagesVisited
    #check what back means
    pagesVisited = ["homepage"]
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

    #returns num options
    optionNum = print_login_menu()
    selection = user_input(optionNum)

    # login option
    if selection == 1:  # log in
        login()

    # signup option
    elif selection == 2:
        signup()

    #   find friends option
    elif selection == 3:
        findfriendsPage()

    # play video (not separate page)
    elif selection == 4:
        print("\nVideo now playing...")
        homepage()

    elif selection == 5:
        usefulLinksPage()
        return

    elif selection == 6:
        importantLinksPage()
        return


    elif selection == 6:
        pass


# -------------------------FindFRIENDS---------------------------------------------------------------

def findfriendsPage():
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
                login()
            elif selection == 2:
                signup()

        else:
            print("\nYour friend has not joined inCollege yet!")
            previous()

    elif selection == 2:
        previous()


#--------------------------useful LINKS------------------------------

def print_useful_links():
    print("\n1. General Page"
          "\n2. Browse in College"
          "\n3. Business Solution"
          "\n4. Directories"
          "\n5. Go Back")

def usefulLinksPage():
    if pagesVisited[-1] != "useful links":
        pagesVisited.append("useful links")

    print_useful_links()
    selection = user_input(5)

    if selection == 1:
        generalPage()

    elif selection == 2:
        browseInCollegePage()

    elif selection == 3:
        businessSolutionsPage()

    elif selection == 4:
        directories()

    elif selection == 5:
        previous()



def generalPage():
    if pagesVisited[-1] != "general":
        pagesVisited.append("general")

#*********************************DEVELOPERS NOTE***************************************************************
#*******************Please follow the scheme of  for example "usefullinksPage() is set up***************
#******************Don't forget to add the according function in previous**********************************
#************************************************************************************************************

#The General group will provide links to Sign Up, Help Center, About, Press, Blog, Careers, and Developers.

# "Sign up" will take the user to the In College sign in processing section.
# "Help Center" will produce the message "We're here to help".
# Selecting "About" displays "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide".
# Selecting "Press" will result in the message "In College Pressroom: Stay on top of the latest news, updates, and reports" being displayed. 
# Selecting "Blog", "Careers", and "Developers" will cause the message "Under construction" to be displayed.

#delete previous() menu is complete
    previous()


def browseInCollegePage():
    if pagesVisited[-1] != "browse in college":
        pagesVisited.append("browse in college")
    previous()
    
def businessSolutionsPage():
    if pagesVisited[-1] != "business solutions":
        pagesVisited.append("business solutions")
    previous()

def directories():
    if pagesVisited[-1] != "directories":
        pagesVisited.append("directories")
    previous()


#-----------------important Links---------------------
def print_important_links():
    print("\n1. Copyright Notice"
          "\n2. About"
          "\n3. Accessbility"
          "\n4. User Agreement"
          "\n5. Privacy Policy"
          "\n6. Cookie Policy"
          "\n7. Copy Right Policy"
          "\n8. Brand Policy"
          "\n9. Guest Controls"
          "\n10. Languages"
          "\n11. Go Back")


def importantLinksPage():
    if pagesVisited[-1] != "important links":
        pagesVisited.append("important links")

    print_important_links()
    selection = user_input(11)

    if selection == 1:
        copyrightNotice()

    elif selection == 2:
        about()

    elif selection == 3:
        accessbility()

    elif selection == 4:
        userAgreement()

    elif selection == 5:
        privacyPolicy()

    elif selection == 6:
        cookiePolicy()

    elif selection == 7:
        copyRightPolicy()

    elif selection == 8:
        brandPolicy()
    
    elif selection == 9:
        guestControls()
    
    elif selection == 10:
        languages()

    elif selection == 11:
        previous()


def copyrightNotice():
    if pagesVisited[-1] != "copyright notice":
        pagesVisited.append("copyright notice")
        #********We get to make up another bull story guys :D*************
    previous()

def about():
    if pagesVisited[-1] != "about":
        pagesVisited.append("about")
    previous()

def accessbility():
    if pagesVisited[-1] != "accessbility":
        pagesVisited.append("directories")
    previous()

def accessibility():
    if pagesVisited[-1] != "accessibility":
        pagesVisited.append("accessibility")
    previous()

def userAgreement():
    if pagesVisited[-1] != "user agreement":
        pagesVisited.append("user agreement")
    previous()

def privacyPolicy():
    guestControls()

def cookiePolicy():
    if pagesVisited[-1] != "cookie policy":
        pagesVisited.append("cookie policy")
    previous()

def copyRightPolicy():
    if pagesVisited[-1] != "copy right policy":
        pagesVisited.append("copy right policy")
    previous()

def brandPolicy():
    if pagesVisited[-1] != "brand policy":
        pagesVisited.append("brand policy")
    previous()

def guestControls():
    if pagesVisited[-1] != "guest controls":
        pagesVisited.append("guest controls")

        #guest control
    #bool inCollegeEmail = true
    #bool SMS = true
    #bool adds = true

    #----------------------DEV TASK-------------------------------------------------------
    #user will be provided with an additional option:
    #"Guest Controls" The Guest Controls option will provide a signed in user with the ability to individually turn off
    #   the InCollege Email, SMS, and Targeted Advertising features. 
    #These options are turned on when an account is created and a user can turn them off. 

    #NOTE
    #if logged in,              need to make a boolean variable to see if user is logged in, and set it falls when it logs out
    #   have user be able to set the variables false (set it false in database) (suggestion: make a row in the login table?)
    #else
    #   store this info to true in database
    previous()

def languages():
    #have fun adding the shit to the database
    if pagesVisited[-1] != "languages":
        pagesVisited.append("languages")
    previous()


# -------------------------EXECUTE---------------------------------------------------------------


homepage()

con.close()