import os
import sqlite3


#about(username, title, major, university, description)''')
#experience(username, job_title, employer , date_start, date_finish, location , e_description)''')
#education(username, school , degree , years)''')                                  
def output_profiles():
    #deletes current file with that name
    open('MyCollege_profiles.txt', 'w').close()

    #creates file again but with new info
    f = open("MyCollege_profiles.txt","w+")


    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    users = tmpcursor.execute("SELECT * FROM about").fetchall()

    for i in users:
        #title, major, univ name, description, experience, and education
        f.write("%s\n%s\n%s\n%s\n" % (i[1], i[2], i[3], i[4]))
        exp = tmpcursor.execute("SELECT * FROM experience WHERE (username = '{}')".format(i[0])).fetchone()
        if(exp != None):
            f.write("%s\n%s\n%s\n%s\n%s\n%s\n" % (exp[1], exp[2], exp[3], exp[4], exp[5], exp[6]))

        edu = tmpcursor.execute("SELECT * FROM education WHERE (username = '{}')".format(i[0])).fetchone()
        if(edu != None):
            f.write("%s\n%s\n%s" % (edu[1], edu[2], edu[3]))

        f.write("=====\n")
    tmpcon.close()
    f.close()

def output_users():
    #deletes current file with that name
    open('MyCollege_users.txt', 'w').close()

    #creates file again but with new info
    f = open("MyCollege_users.txt","w+")


    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    users = tmpcursor.execute("SELECT * FROM users").fetchall()

    for i in users:
        if i[4] == 2:
            tmp = "Plus"
        else:
            tmp = "Standard"
        f.write("%s %s\n" % (i[2], tmp))
    tmpcon.close()
    f.close()

def output_training():
    #deletes current file with that name
    open('MyCollege_training.txt', 'w').close()

    #creates file again but with new info
    f = open("MyCollege_training.txt","w+")


    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    courses = tmpcursor.execute("SELECT * FROM courses ORDER BY username").fetchall()
    prev = " "
    for i in courses:
        if i[1] != prev and prev != " ":
            f.write("=====\n")

        f.write("%s\t%s\n" % (i[1], return_course_name(i[0])))
        prev = i[1]

    tmpcon.close()
    f.close()


#jobs(username, title, description, employer, location, salary)
#app_status(username, title, posted, status)
#applications(username, title, employer, grad_date, start_date, best_fit)
def output_appliedJobs():
    #deletes current file with that name
    open('MyCollege_appliedJobs.txt', 'w').close()

    #creates file again but with new info
    f = open("MyCollege_appliedJobs.txt","w+")


    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    applied = tmpcursor.execute("SELECT * FROM jobs ORDER BY title").fetchall()
    prev = " "
    for i in applied:
        f.write("%s\n" % (i[1]))

        #forloop
        applications = tmpcursor.execute("SELECT * FROM applications WHERE (title = '{}' COLLATE NOCASE) ORDER BY username".format(i[1])).fetchall()
        for apps in applications:
            f.write("%s %s\n" % (apps[0], apps[5]))

        f.write("=====\n")

    tmpcon.close()
    f.close()


def output_savedJobs():
    #deletes current file with that name
    open('MyCollege_savedJobs.txt', 'w').close()

    #creates file again but with new info
    f = open("MyCollege_savedJobs.txt","w+")


    tmpcon = sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    users = tmpcursor.execute("SELECT * FROM users ORDER BY username").fetchall()
    prev = " "
    for i in users:
        f.write("%s\n" % (i[2]))

        #forloop
        applications = tmpcursor.execute("SELECT * FROM app_status WHERE (username = '{}' AND status = 'saved' COLLATE NOCASE) ORDER BY username".format(i[2])).fetchall()
        for apps in applications:
            f.write("%s\n" % (apps[1]))

        f.write("=====\n")

    tmpcon.close()
    f.close()


def return_course_name(num):
    if num == 1:
        return "How to use In College learning"
    elif num == 2:
        return "Train the trainer"
    elif num == 3:
        return "Gamification of learning"
    elif num == 4:
        return "Understanding the Architectural Design Process"
    elif num == 5:
        return "Project Management Simplified"
    else:
        return "How to not be dumb"