import database as db
import pages as pg


# *********************************DEVELOPERS ***************************************************************
# *******************Please follow the scheme of  for example "usefullinksPage() is set up***************
# ******************Don't forget to add the according function in previous**********************************
# ************************************************************************************************************

    # ----------------------DEV TASK-------------------------------------------------------
    # user will be provided with an additional option:
    # "Guest Controls" The Guest Controls option will provide a signed in user with the ability to individually turn off
    #   the InCollege Email, SMS, and Targeted Advertising features.
    # These options are turned on when an account is created and a user can turn them off.
    # if logged in need to make a boolean variable to see if user is logged in, and set it falls when it logs out
    # have user be able to set the variables false (set it false in database) (suggestion: make a row in the login table?)
    # else
    #   store this info to true in database
    # pv.previous()


#new note:
# 0 is the new default for Go Back. This is implemented in the user_input function in the menu file

# -------------------------EXECUTE---------------------------------------------------------------

def main():
    pg.homepage()
    db.con.close()
    
if __name__ == "__main__":
    main()

