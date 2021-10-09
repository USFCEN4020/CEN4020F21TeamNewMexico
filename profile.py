import prev_page as pv
import database as db
import pages as pg


#--------------------ABOUT SESSION-------------------
def aboutProfilePage(uName):
    if pg.pagesVisited[-1] != "aboutProfile":
        pg.pagesVisited.append("aboutProfile")
        
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    
    tmpcursor.execute("SELECT * FROM about WHERE username = ?", (uName,))
    p_about = tmpcursor.fetchone()
    print("\nlast saved: ")
    print(p_about)
    
    print("\nIn the ABOUT page you will be creating a title, Selecting your major , university and writing a description\n")

    if p_about == None:
      tmpcursor.execute("INSERT INTO about VALUES (?, ?, ?, ?, ?)",
      (uName,
      input("\nTitle of your profile: "),                  input("\nWhat is your Major: ").title(),                     input("\nWhat is your university: ").title(),
      input ("\nWrite a discription for your profile: ")))
    else: 
      tmpcursor.execute("UPDATE about SET  title = ?, major = ? , university = ?, description = ? where username = ?", 
      (input("\nTitle of your profile: "),                 input("\nWhat is your Major: ").title(),                     input("\nWhat is your university").title(),
      input ("\nWrite a discription for your profile"),uName))
    
    tmpcon.commit()
    tmpcursor.execute("SELECT * FROM about WHERE username = ?", (uName,))
    p_about = tmpcursor.fetchone()
    tmpcon.close()
    print("\nsuccessfully saved: ")
    print(p_about)
    pv.previous()

#----------------------experience session----------------
def experiencePage(uName):
    if pg.pagesVisited[-1] != "experience":
        pg.pagesVisited.append("experience")
        
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    
    tmpcursor.execute("SELECT * FROM experience WHERE username = ?", (uName,))
    exp = tmpcursor.fetchall()
    print("\nlast saved: ")
    print(exp)
    
    print("\nIn the Experience page you will be creating a job title, employer, Date started, date ended, location, and job description  \n")
    
    if len(exp) < 3:
      tmpcursor.execute("INSERT INTO experience VALUES (?, ?, ?, ?, ?, ?, ? )",
      (uName,
      input("\nTitle of the JOB : "),                   input("\nWho is/was the employer: "),                input("\nDate Started: "),
      input("\nDate ended: "),
      input("\nLocation: "),
      input ("\nDescribe Your responsabilities ")))
    else:
      print ("\nJob History Full (up to 3 jobs)")

    tmpcon.commit()
    tmpcursor.execute("SELECT * FROM experience WHERE username = ?", (uName,))
    exp = tmpcursor.fetchall()
    tmpcon.close()

    print("\nsuccessfully saved: ")
    print(len(exp))
    pv.previous()

#--------------------EDUCATION SESSION-------------------
def educationPage(uName):
    if pg.pagesVisited[-1] != "education":
        pg.pagesVisited.append("education")
        
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    
    tmpcursor.execute("SELECT * FROM education WHERE username = ?", (uName,))
    edu = tmpcursor.fetchone()
    print("\nlast saved: ")
    print(edu)
    
    print("\nIn the EDUCATION SECTION you will be updating your school , degree and years \n")

# (username, school , date_start, degree , years)'''
    if edu == None:
      tmpcursor.execute("INSERT INTO education VALUES (?, ?, ?, ?)",
      (uName,
      input("\nName of the School: ").title(),                   input("\nHighest Degree: "),                        input("\nYears Attended: ")))
    else:
      tmpcursor.execute("UPDATE education SET  school = ?, degree = ? , years = ? where username = ?",       (input("\nName of the School: ").title(),                   input("\nHighest Degree: "),                        input("\nYears Attended: "),
    uName))
    
    tmpcon.commit()
    tmpcursor.execute("SELECT * FROM education WHERE username = ?", (uName,))
    edu = tmpcursor.fetchone()
    tmpcon.close()

    print("\nsuccessfully saved: ")
    print(edu)
    pv.previous()

#-------------------------view profile--------------
def viewProfilePage(uName):
    if pg.pagesVisited[-1] != "view-profile":
        pg.pagesVisited.append("view-profile")
    
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    
    tmpcursor.execute("SELECT * FROM about WHERE username = ?", (uName,))
    about = tmpcursor.fetchone()
    
    if about == None:
        print ("\n YOU have Not yet completed the About section of your profile. Please review your ABOUT Section")
    else:    
        print("\nPROFILE BY {}: "
              "\n--------------ABOUT SECTION-------- ->"
              "\nProfile Title: {}"                   "\nMajor: {}"                       
               "\nUniversity: {}"
               "\nAbout: {} \n".format(about[0], about[1], about[2], about[3], about[4]))
    
    
    tmpcursor.execute("SELECT * FROM experience WHERE username = ?", (uName,))
    exp = tmpcursor.fetchall()
    row_exp = len(exp)
    print(row_exp)
    if row_exp == None:
        print ("\n YOU have Not yet completed the EXPIRIENCE section of your profile. Please review your EXPIRIENCE Section")
    
    elif row_exp == 1 :    
        print("--------------EXPERIENCE SECTION--------->"
          "\nJOB 1 Title : {}"
          "\nWho is/was the employer: {}"
          "\nDate Started: {}"
          "\nDate ended: {}"
          "\nLocation: {}"
          "\nResponsabilities {}".format(exp[0][1], exp[0][2], exp[0][3], exp[0][4], exp[0][5],exp[0][6]))
    
    elif row_exp == 2 :    
      print("--------------EXPERIENCE SECTION--------->"
          "\nJOB 1 Title : {}"
          "\nWho is/was the employer: {}"
          "\nDate Started: {}"
          "\nDate ended: {}"
          "\nLocation: {}"
          "\nResponsabilities {}".format(exp[0][1], exp[0][2], exp[0][3], exp[0][4], exp[0][5],exp[0][6]))
      print(
          "\nJOB 2 Title : {}"
          "\nWho is/was the employer: {}"
          "\nDate Started: {}"
          "\nDate ended: {}"
          "\nLocation: {}"
          "\nResponsabilities {}".format(exp[1][1], exp[1][2], exp[1][3], exp[1][4], exp[1][5],exp[1][6]))
    
    elif row_exp == 3:    
        print("--------------EXPERIENCE SECTION--------->"
          "\nJOB 1 Title : {}"
          "\nWho is/was the employer: {}"
          "\nDate Started: {}"
          "\nDate ended: {}"
          "\nLocation: {}"
          "\nResponsabilities {}".format(exp[0][1], exp[0][2], exp[0][3], exp[0][4], exp[0][5],exp[0][6]))
        print(
          "\nJOB 2 Title : {}"
          "\nWho is/was the employer: {}"
          "\nDate Started: {}"
          "\nDate ended: {}"
          "\nLocation: {}"
          "\nResponsabilities {}".format(exp[1][1], exp[1][2], exp[1][3], exp[1][4], exp[1][5],exp[1][6]))
        print(
          "\nJOB 3 Title : {}"
          "\nWho is/was the employer: {}"
          "\nDate Started: {}"
          "\nDate ended: {}"
          "\nLocation: {}"
          "\nResponsabilities {}".format(exp[2][1], exp[2][2], exp[2][3], exp[2][4], exp[2][5],exp[2][6]))
    
    tmpcursor.execute("SELECT * FROM education WHERE username = ?", (uName,))
    edu = tmpcursor.fetchone()
    if edu == None:
        print ("\n YOU have Not yet completed the About section of your profile. Please review your ABOUT Section")
    else:    
        print(
              "\n--------------EDUCATION SECTION-------- ->"
              "\nProfile Title: {}"                   "\nMajor: {}"                       
               "\nUniversity: {}"
               "\nAbout: {} \n".format(edu[0], edu[1], edu[2], edu[3]))

    pv.previous()
  

    
    
    