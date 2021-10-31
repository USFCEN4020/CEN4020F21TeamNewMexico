import prev_page as pv

#0 is default to go to the previous page
def user_input(maxInput):
    my_selection = input("\nEnter your selection: ")
    # cast to int
    numSelection = int(my_selection)  # might cause casting error like if my_selection is alpha
    if numSelection == 0:
        return pv.previous()
    while not my_selection.isnumeric() or (numSelection > maxInput or numSelection < 1):
        my_selection = input("\nPlease enter a valid selection: ")
        numSelection = int(my_selection)

    return int(my_selection)

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
          "\n10. Log Out")


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
          "\n7. Exit")
    
    # ****NOTE*******
    # Change this number when we add options
    optionNum = 7
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

          
