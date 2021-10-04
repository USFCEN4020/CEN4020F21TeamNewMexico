import prev_page as pv
import registration as reg
import menus as menu
import jobs as job
import friends as friend
import database as db

# NOTE 

# 1) make sure to separate EVERY individual page in a different function
# 2) Add the new page created to the previous() with the according string and function
# 3) also DON'T FORGET to append the page to the vistedPages list
# 4) make sure you change the parameter of user_input() when the size of the menu changes

# changes
# added job_post_function
# made pagesVisited list global. Now it doesn't need to be passed through every page's parameter anymore



# --------------------------GO TO PAGE---------------------------
# ****************************add to this list as we make new pages*********
def user_input(maxInput):
    my_selection = input("\nEnter your selection: ")
    # cast to int
    numSelection = int(my_selection)  # might cause casting error like if my_selection is alpha
    while not my_selection.isnumeric() or (numSelection > maxInput or numSelection < 1):
        my_selection = input("\nPlease enter a valid selection: ")
        numSelection = int(my_selection)

    return int(my_selection)

# ------------------------------HOMEPAGE---------------------

def homepage():
    # when at the homepage menu, you shouldn't have access to prev
    global login_flag
    login_flag = False
    global pagesVisited
    # check what back means
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

    # returns num options
    optionNum = menu.print_login_menu()
    selection = user_input(optionNum)

    # login option
    if selection == 1:  # log in
        login_flag = True
        reg.login()
        

    # signup option
    elif selection == 2:
        reg.signup()

    #   find friends option
    elif selection == 3:
        print("\nVideo now playing...")
        homepage()

    # play video (not separate page)
    elif selection == 4:
        findfriendsPage()

    elif selection == 5:
        usefulLinksPage()
        return

    elif selection == 6:
        importantLinksPage()
        return


    elif selection == 7:
        pass

# ---------------------------------MAINPAGE--------------------------------------------------------------

def mainPage():
    if not pagesVisited:
        pagesVisited.append("mainpage")
    elif pagesVisited[-1] != "mainpage":
        pagesVisited.append("mainpage")
    menu.print_options_menu()
    selection = user_input(6)

    # added code
    # sub_selection = None

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

    elif selection == 6:
        homepage()


#SKILL PAGE
# FUNCTIONS TO IMPLEMENT LATER
def pythonPage():
    if pagesVisited[-1] != "python":
        pagesVisited.append("python")
    print("\nThis page is currently under construction. Come back soon!")
    pv.previous()


def javaPage():
    if pagesVisited[-1] != "java":
        pagesVisited.append("java")
    print("\nThis page is currently under construction. Come back soon!")
    pv.previous()


def cPage():
    if pagesVisited[-1] != "c":
        pagesVisited.append("c")
    print("\nThis page is currently under construction. Come back soon!")
    pv.previous()


def cppPage():
    if pagesVisited[-1] != "c++":
        pagesVisited.append("c++")
    print("\nThis page is currently under construction. Come back soon!")
    pv.previous()


def rubyPage():
    if pagesVisited[-1] != "ruby":
        pagesVisited.append("ruby")
    print("\nThis page is currently under construction. Come back soon!")
    pv.previous()


def skillsPage():
    if pagesVisited[-1] != "skills":
        pagesVisited.append("skills")
    menu.print_skills_menu()
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
        pv.previous()


# --------------------------------FRIENDS--------------------------------------

def friendsPage():
    if pagesVisited[-1] != "friends":
        pagesVisited.append("friends")

        pv.previous()


def jobPage():
    if pagesVisited[-1] != "jobs":
        pagesVisited.append("jobs")
    print("\n1. Post a job"
          "\n2. Go back")

    selection = user_input(2)

    if selection == 1:
        job.post_job_page()

    elif selection == 2:
        pv.previous()


# -------------------------FindFRIENDS---------------------------------------------------------------

def findfriendsPage():
    pagesVisited.append("findfriends")
    print("\n1. Look for a friend"
          "\n2. Go back")

    selection = user_input(2)

    if selection == 1:
        first = input("\nFirst name: ")
        last = input("\nLast name: ")
        if friend.find_friend_account(first, last):
            print("\nYour friend is on inCollege! Join them today."
                  "\n1. Log in"
                  "\n2. Sign up")

            selection = user_input(2)

            if selection == 1:
                reg.login()
            elif selection == 2:
                reg.signup()

        else:
            print("\nYour friend has not joined inCollege yet!")
            pv.previous()

    elif selection == 2:
        pv.previous()

def usefulLinksPage():
    if pagesVisited[-1] != "useful links":
        pagesVisited.append("useful links")

    menu.print_useful_links()
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
        pv.previous()


#-----------------LINKS PAGE--------------------#
def generalPage():
    if pagesVisited[-1] != "general":
        pagesVisited.append("general")

    menu.print_general_menu()
    selection = user_input(8)

    if selection == 1:
        reg.signup()

    elif selection == 2:
        helpCenterPage()

    elif selection == 3:
        about()

    elif selection == 4:
        pressPage()

    elif selection == 5:
        BlogPage()

    elif selection == 6:
        carrierPage()

    elif selection == 7:
        devPage()

    elif selection == 8:
        pv.previous()

def helpCenterPage():
    if pagesVisited[-1] != "help center":
        pagesVisited.append("help center")
    print("We're here to help. ")
    pv.previous()


def pressPage():
    if pagesVisited[-1] != "press":
        pagesVisited.append("press")
    print("In College Pressroom: Stay on top of the latest news, updates, and reports")
    pv.previous()


def BlogPage():
    if pagesVisited[-1] != "blog":
        pagesVisited.append("blog")
    print("In College Pressroom: Stay on top of the latest news, updates, and reports")
    pv.previous()


def carrierPage():
    if pagesVisited[-1] != "carrier":
        pagesVisited.append("carrier")
    print("Under Construction")
    pv.previous()


def devPage():
    if pagesVisited[-1] != "developer":
        pagesVisited.append("developer")
    print("Under Construction")
    pv.previous()


# delete pv.previous() menu is complete
# pv.previous()


def browseInCollegePage():
    if pagesVisited[-1] != "browse in college":
        pagesVisited.append("browse in college")
    pv.previous()


def businessSolutionsPage():
    if pagesVisited[-1] != "business solutions":
        pagesVisited.append("business solutions")
    pv.previous()


def directories():
    if pagesVisited[-1] != "directories":
        pagesVisited.append("directories")
    pv.previous()


# -----------------important Links---------------------


def importantLinksPage():
    if pagesVisited[-1] != "important links":
        pagesVisited.append("important links")

    menu.print_important_links()
    selection = user_input(10)

    if selection == 1:
        copyrightNotice()

    elif selection == 2:
        about()

    elif selection == 3:
        accessibility()

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
        pv.previous()


def copyrightNotice():
    if pagesVisited[-1] != "copyright notice":
        pagesVisited.append("copyright notice")
        print("Copyright 2021 inCollege LLC All rights reserved. "
              "\ninCollege© 4202 E Fowler Ave, Tampa, FL 33620")
    pv.previous()


def about():
    if pagesVisited[-1] != "about":
        pagesVisited.append("about")
    print(
        "\nIn College: Welcome to In College, the world's largest college student network "
        "with many users in many countries and territories worldwide.")
    pv.previous()


def accessibility():
    if pagesVisited[-1] != "accessibility":
        pagesVisited.append("accessibility")
    print(
        "\nWe’re committed to accessibility. It is our policy to ensure that everyone, including persons "
        "with disabilities, has full and equal access to our digital offerings.")
    pv.previous()


def userAgreement():
    if pagesVisited[-1] != "user agreement":
        pagesVisited.append("user agreement")
    print("\nUsing inCollege you agree to follow and behave with in the policies of dictated "
          "in the inCollege software. ")
    pv.previous()


def privacyPolicy():
    #if pagesVisited[-1] != "privacy policy":
    #    pagesVisited.append("privacy policy")
    print("\nPrivacy Policy"
          "\nLast updated: October 1, 2021"
          "\ninCollege collects personal information and usage data of the user. "
          "Information recorded from the user is private and secure. "
          "\nIf you have any questions, reach out to privacy@inCollege.com "
          "\ninCollege© 4202 E Fowler Ave, Tampa, FL 33620")
    guestControls()
    #pv.previous()


def cookiePolicy():
    if pagesVisited[-1] != "cookie policy":
        pagesVisited.append("cookie policy")
    print(
        "\nUsing inCollege you agree to share data  may use cookies, web beacons, "
        "tracking pixels, and other tracking technologies when you visit our website, "
        "including any other media form, media channel, mobile website, or mobile application "
        "related or connected.")
    pv.previous()


def copyRightPolicy():
    if pagesVisited[-1] != "copy right policy":
        pagesVisited.append("copy right policy")
    print("\nThe InCollege program reserves all the rights and may not be copied or "
          "duplicated without prior agreement")
    pv.previous()


def brandPolicy():
    if pagesVisited[-1] != "brand policy":
        pagesVisited.append("brand policy")
    print("\nThe InCollege program aims to connect every college student to flourish "
          "relationships and network")
    pv.previous()


def guestControls():
    global login_flag
    if pagesVisited[-1] != "guest controls":
        pagesVisited.append("guest controls")

    if login_flag == True:
        loginControl(reg.username)
        pv.previous()

    else:
        menu.guestControlMenu()
        selection = user_input(1)
        if selection == 1:
            pv.previous()


def loginControl(uName):

    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    tmpcursor.execute("SELECT * FROM settings WHERE username = ?", (uName,))
    settings = tmpcursor.fetchone()

    print("\nSETTINGS BY {}: "
          "\ninCollegeEmail -> {}"
          "\nSMS -> {}"
          "\nads -> {}"
          "\nLanguage -> {}".format(settings[0], settings[1], settings[2], settings[3], settings[4]))
    print("Would you like to change the default settings? \n1.Yes\n2.No")

    selection = user_input(2)
    if selection == 1:
        print("Please ON or OFF for the following settings")

        my_email = on_off_mail()
        my_sms = on_off_sms()
        my_ads = on_off_ads()
        my_language = language()

        tmpcursor.execute("UPDATE settings SET email = ?, SMS = ? , ads = ?, language = ? where username = ?",
                          (my_email, my_sms, my_ads, my_language, reg.username))
        tmpcon.commit()

        print("Changes were successfully")

    elif selection == 2:
        pv.previous()


def on_off_mail():
    print("\ninCollegeEmail \n1.ON \n2.OFF ")
    selection = user_input(2)
    if selection == 1:
        my_email = "ON"
        return my_email
    else:
        my_email = "OFF"
        return my_email


def on_off_sms():
    print("\nSMS \n1.ON \n2.OFF ")
    selection = user_input(2)
    if selection == 1:
        my_sms = "ON"
        return my_sms

    else:
        my_sms = "OFF"
        return my_sms


def on_off_ads():
    print("\nAds \n1.ON \n2.OFF ")
    selection = user_input(2)
    if selection == 1:
        my_ads = "ON"
        return my_ads

    else:
        my_ads = "OFF"
        return my_ads


def language():
    print("\nLanguage \n1.English \n2.Spanish ")
    selection = user_input(2)
    if selection == 1:
        my_lang = "English"
        return my_lang

    else:
        my_lang = "Spanish"
        return my_lang


