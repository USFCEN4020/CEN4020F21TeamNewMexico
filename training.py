import database as db
import pages as page
import prev_page as pv
import registration as reg
import menus as menu

def check_courses(selection):
    if page.pagesVisited[-1] != "courses":
        page.pagesVisited.append("courses")
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    alltakencourses = tmpcursor.execute( "SELECT * FROM courses WHERE (username = '{}' COLLATE NOCASE)".format(reg.username))
    rows = alltakencourses.fetchall()
    
    #testing print(rows)

    if  rows == None:
        tmpcursor.execute("INSERT INTO courses VALUES(? , ?)" , (selection ,  reg.username)) 
        tmpcon.commit()
        tmpcon.close()
        print("\nYou have now completed this training ")
        
    else:
        takencourse = tmpcursor.execute( "SELECT * FROM courses WHERE (username = '{}' COLLATE NOCASE)".format(reg.username)).fetchall()
        if any (selection in i for i in takencourse):
            menu.print_takencourse_menu()
            tmpcon.close()
        else:
            tmpcursor.execute("INSERT INTO courses VALUES(? , ?)" , (selection ,  reg.username)) 
            tmpcon.commit()
            tmpcon.close()
            print("\nYou have now completed this training ")
            

def inCollegeLearningPage():  
    if page.pagesVisited[-1] != "inCollege Learning":
        page.pagesVisited.append("inCollege Learning")
    
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    tmpcon.commit()
    courses = tmpcursor.execute('Select courses from coursenames').fetchall()
    for i in range(0, len(courses)):
        print("{}. Course {}: {}".format((i + 1), i + 1, courses[i][0]))
    print('\nEnter 0 to go back\n')
    selection = menu.user_input(len(courses))

    check_courses(selection)
    pv.previous()
    
    #if selection == 1:
        #check_courses(1)
        #pv.previous()
    #elif selection == 2:
        #check_courses(2)
        #pv.previous()
    #elif selection == 3:
        #check_courses(3)
        #pv.previous()
    #elif selection == 4:
        #check_courses(4)
        #pv.previous()
    #elif selection == 5:
        #check_courses(5)
        #pv.previous()
            
      