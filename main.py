import database as db
import pages as pg
from os.path import exists
import registration as rg
import jobs as jb


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
    locatestudentAccouts = exists('studentAccouts.txt')
    locatenewJobs = exists('newJobs.txt')
    locatenewtraining = exists('newtraining.txt')
    if locatestudentAccouts:
        with open('studentAccouts.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                if i % 3 == 0 or i == 0:
                    lines[i] = lines[i].split()
                else:
                    lines[i] = lines[i].strip()
            count = 0
            uName = None
            passw = None
            fName = None
            lName = None
            for i in range(0, len(lines)):
                if not rg.space_for_signup():
                    print('No more space to create new accounts')
                    break
                elif lines[i] == '=====' and rg.space_for_signup():
                    rg.create_user(uName, passw, fName, lName, None)
                    count = 0
                    uName = passw = fName = lName = None
                elif count == 0:
                    uName = lines[i][0]
                    fName = lines[i][1]
                    lName = lines[i][2]
                    count += 1
                elif count == 1:
                    passw = lines[i]
                    count += 1
            line = ''
    if locatenewJobs:
        with open('newJobs.txt', 'r') as file:
            result = []
            temp = ''
            line = ''
            count = 0
            while True:
                line = file.readline()
                if not line:
                    line = ''
                    break
                elif count == 0:
                    result.append(line)
                    count += 1
                elif count == 1:
                    while '&&&' not in line:
                        temp += line
                        line = file.readline()                        
                    temp = temp.replace('&&&', '')
                    temp = temp.strip(' \n')
                    result.append(temp)
                    count += 1
                elif count == 2:
                    while '=====' not in line:
                        if '&&&' not in line:                            
                            result.append(line)
                            line = file.readline()
                        else:
                            line = file.readline()
                    for i in range(0, len(result)):
                        result[i] = result[i].strip()
                    jb.post_job(result[0], result[1], result[3], result[4], result[5], result[2], True)
                    result.clear()
                    temp = ''
                    count = 0

    if locatenewtraining:
        with open('newtraining.txt', 'r') as file:
            while True:
                line = file.readline()
                line = line.strip()
                if not line:
                    line = ''
                    break
                else:
                    tmpcon = db.sqlite3.connect('inCollege.db')
                    tmpcursor = tmpcon.cursor()
                    tmpcursor.execute("INSERT INTO coursenames VALUES('{}')".format(line))
                    tmpcon.commit()
                    tmpcon.close()

    jb.write_jobs()
    pg.homepage()
    db.con.close()
    
if __name__ == "__main__":
    main()

