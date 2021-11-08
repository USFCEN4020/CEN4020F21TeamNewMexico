import messages
import prev_page as pv
import registration as reg
import menus as menu
import jobs as job
import friends as friend
import database as db
import profile as pf
import messages as msg

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
    selection = menu.user_input(optionNum)

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
        friend.findfriendsPage()

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

    #prints pending friends
    if friend.pending_friend(reg.username) == True:
        print("You have a pending friend request")
    else:
        print("no friend requests :(")

    if job.job_deleted(reg.username) == True:
        print("A job you have saved or applied for has been Deleted.")

    if messages.inboxNotification():
        print("\nYou have messages in your inbox.")

    menu.print_options_menu()
    selection = menu.user_input(10)

    # added code
    # sub_selection = None
    
    if selection == 1:
        profilePage()

    # goTo jobs
    elif selection == 2:
        job.jobPage()

    # goTo friends
    elif selection == 3:
        friend.friendsPage()

    elif selection == 4:
        friend.view_pending_requests()

    elif selection == 5:
        show_network()

    elif selection == 6:
        msg.messagesPage(reg.username)

# goTo skills
    elif selection == 7:
        skillsPage()

    elif selection == 8:
        usefulLinksPage()

    elif selection == 9:
        importantLinksPage()

    elif selection == 10:
        homepage()

#_-----friends--------

def show_network():
    connections = None
    result = db.cursor.execute("SELECT firstName, lastName, username, status FROM friends "
                               "NATURAL JOIN users WHERE friends_user = '{}'".format(reg.username)).fetchall()
    if len(result) == 0:
        print("\nYou have no connections yet.")
        conections = False

    while(True):
      count = 1
      for i in result:

        print("{}. {} {} Username: {} Status: {}" .format(count, i[0], i[1], i[2], i[3]))
        count += 1
        connections = True

      print("\n0. GO BACK\n")
      selection = input("Please enter line number to view connection options:")
      
      if int (selection) == 0:
        mainPage()
        return

      if int(selection) < 1 or int(selection) > len(result):
        print("\nInvalid entry please re-enter.")
        continue
      else:
        friendConnection = result[int(selection) - 1][2]

        print("1. View user's profile\n"
              "2. Disconnect from friend\n"
              "0. Go back\n")
        print("\nEnter Selection: ")
        selection = menu.user_input(2)
        if int(selection) == 1:
            pf.viewProfilePage(friendConnection, True)
        elif int(selection) == 2:
            db.cursor.execute("DELETE FROM friends WHERE username = '{}' AND friends_user = '{}'".format(reg.username, friendConnection))
            db.cursor.execute("DELETE FROM friends WHERE username = '{}' AND friends_user = '{}'".format(friendConnection, reg.username))
            db.con.commit()
            mainPage()
        elif int(selection) == 0:
            mainPage()
            break
        
  

#--------------profile page--------------

def profilePage():

    if pagesVisited[-1] != "profile":
        pagesVisited.append("profile")
    menu.profileMenu()
    selection = menu.user_input(5)

    if selection == 1:
        pf.aboutProfilePage(reg.username)
    elif selection == 2:
        pf.experiencePage(reg.username)
    elif selection == 3:
        pf.educationPage(reg.username)
    elif selection == 4:
        pf.viewProfilePage(reg.username)
    elif selection == 5:
        msg.messagesPage(reg.username)

    
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
    selection = menu.user_input(6)

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







# -------------------------usefulLinksPage---------------------------------------------------------------



def usefulLinksPage():
    if pagesVisited[-1] != "useful links":
        pagesVisited.append("useful links")

    menu.print_useful_links()
    selection = menu.user_input(4)

    if selection == 1:
        generalPage()

    elif selection == 2:
        browseInCollegePage()

    elif selection == 3:
        businessSolutionsPage()

    elif selection == 4:
        directories()


#-----------------LINKS PAGE--------------------#
def generalPage():
    if pagesVisited[-1] != "general":
        pagesVisited.append("general")

    menu.print_general_menu()
    selection = menu.user_input(7)

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
    selection = menu.user_input(9)

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
        selection = menu.user_input(1)
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

    selection = menu.user_input(2)
    if selection == 1:
        print("Please ON or OFF for the following settings")

        my_email = on_off_mail()
        my_sms = on_off_sms()
        my_ads = on_off_ads()
        my_language = language()

        tmpcursor.execute("UPDATE settings SET email = ?, SMS = ? , ads = ?, language = ? where username = ?",
                          (my_email, my_sms, my_ads, my_language, reg.username))
        tmpcon.commit()
        tmpcon.close()
        print("\nChanges were successfully")

    elif selection == 2:
        pv.previous()


def on_off_mail():
    print("\ninCollegeEmail \n1.ON \n2.OFF ")
    selection = menu.user_input(2)
    if selection == 1:
        my_email = "ON"
        return my_email
    else:
        my_email = "OFF"
        return my_email


def on_off_sms():
    print("\nSMS \n1.ON \n2.OFF ")
    selection = menu.user_input(2)
    if selection == 1:
        my_sms = "ON"
        return my_sms

    else:
        my_sms = "OFF"
        return my_sms


def on_off_ads():
    print("\nAds \n1.ON \n2.OFF ")
    selection = menu.user_input(2)
    if selection == 1:
        my_ads = "ON"
        return my_ads

    else:
        my_ads = "OFF"
        return my_ads


def language():
    print("\nLanguage \n1.English \n2.Spanish ")
    selection = menu.user_input(2)
    if selection == 1:
        my_lang = "English"
        return my_lang

    else:
        my_lang = "Spanish"
        return my_lang



            
