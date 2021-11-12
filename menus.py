import prev_page as pv
import pages as page

#0 is default to go to the previous page
def user_input(maxInput, bypassPrev = False):
    try:
        my_selection = int(input("\nEnter your selection: "))
        # Convert it into integer
        print("Input is an integer number. Number = ", my_selection)
        if (my_selection <= maxInput and my_selection >= 1):
            return my_selection
        elif my_selection == 0:
            if not bypassPrev:
                return pv.previous()
            else:
                return 0
        else:
            print("\nPlease enter a valid number from 1 to {} ".format(maxInput))
            user_input(maxInput)
    except ValueError:
            print("No.. input is not a number. It's a string")
            print("\nPlease enter a valid number from 1 to {} ".format(maxInput))
            return user_input(maxInput)
    # my_selection = int(input("\nEnter your selection: "))
    # if my_selection.isnumeric() and (my_selection > maxInput or my_selection < 1):
    #     numSelection = int(my_selection)
    #     if numSelection == 0:
    #         return pv.previous()
    #     else:
    #         return int(my_selection)
    # # cast to int
    # # numSelection = int(my_selection)  # might cause casting error like if my_selection is alpha
    # else:
    #     while not my_selection.isnumeric() or (numSelection > maxInput or numSelection < 1):
    #         print("\nPlease enter a valid number from 1 to {} ".format(maxInput))
    #         user_input(maxInput)

   

def printMessageOptions():
    print("What would you like to do?"
           "\n0. Go back to main menu"
           "\n1. Go to Inbox "
           "\n2. Send a message "
        )
def printSenderOptions():
    print("0. Go back to messages"
        "\n1. Send a message to a friend"
        "\n2. Send a message to someone in inCollege")

def print_options_menu():
    print("\n1. Create/Modify Profile"
          "\n2. Job/Internship Search"
          "\n3. Search For a friend"
          "\n4. Pending friend request"
          "\n5. Show my network"
          "\n6. Go to Messages"
          "\n7. Learn a new skill"
          "\n8. Useful Links"
          "\n9. InCollege Important Links"
          "\n10. InCollege Learning"
          "\n11. Log Out")


def print_skills_menu():
    print("\nSkills:"
          "\n0. go Back"
          "\n1. Python"
          "\n2. Java"
          "\n3. C"
          "\n4. C++"
          "\n5. Ruby"
                    )

def print_login_menu():
    print("\n1. Log In"
          "\n2. Sign Up"
          "\n3. Watch Our Video"
          "\n4. Search for a Friend"
          "\n5. Useful Links"
          "\n6. Important Links"
          "\n7. Training"
          "\n8. Exit")
    
    # ****NOTE*******
    # Change this number when we add options
    optionNum = 8
    return optionNum


def print_useful_links():
    print("0. go Back"
          "\n1. General Page"
          "\n2. Browse in College"
          "\n3. Business Solution"
          "\n4. Directories")


def print_general_menu():
    print("\n0. Go Back"
          "\n1. Sign Up"
          "\n2. Help Center"
          "\n3. About"
          "\n4. Press"
          "\n5. Blog"
          "\n6. Carrier"
          "\n7. Developer")

def print_important_links():
    print("\n0. Go Back"
          "\n1. Copyright Notice"
          "\n2. About"
          "\n3. Accessibility"
          "\n4. User Agreement"
          "\n5. Privacy Policy"
          "\n6. Cookie Policy"
          "\n7. Copy Right Policy"
          "\n8. Brand Policy"
          "\n9. Guest Controls")


def guestControlMenu():
    print("\nSETTINGS BY DEFAULT: "
          "\ninCollegeEmail -> ON"
          "\nSMS -> ON"
          "\nads -> ON"
          "\nLanguage -> English"
          "\nType 1 to Go Back")

def profileMenu():
    print("\nWould you like to modify your Profile\n"
          "\n0. Go Back"
          "\n1. About"
          "\n2. Experience"
          "\n3. Education"
          "\n4. View Profile"
          "\n5. Message")

def profilejobMenu():
   print("--------------EXPERIENCE SECTION--------->"
          "\nJOB 1 Title : {}"
          "\nWho is/was the employer: {}"
          "\nDate Started: {}"
          "\nDate ended: {}"
          "\nLocation: {}"
          "\nResponsabilities {}")

#inCollege learning menu epic9
def print_inCollegeLearning_menu():
    print("\n1. Course 1: How to use In College learning"
          "\n2. Course 2: Train the trainer"
          "\n3. Course 3: Gamification of learning"
          "\n4. Course 4: Understanding the Architectural Design Process"
          "\n5. Course 5: Project Management Simplified"
          "\n0. Go Back")       

def print_takencourse_menu():
    print("\nYou have already taken this course, do you want to take it again?")
    selection = input("Please enter YES or NO")
    selection.lower()
    if selection == "yes":
        print("\nYou have now re-completed this training ")
    elif selection == "no":
        print("\nCourse Cancelled ")
    else:
        print("invalid entry")  
