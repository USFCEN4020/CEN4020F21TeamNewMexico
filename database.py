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

cursor.execute('''CREATE TABLE IF NOT EXISTS settings
                 (username, email, SMS, ads, language)''')

#handling PROFILE                           
cursor.execute('''CREATE TABLE IF NOT EXISTS about
                 (username, title, major, university, description)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS experience
                 (username, job_title, employer , date_start, date_finish, location , e_description)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS education
                 (username, school , degree , years)''')                                  


# how i see it
# each user needs their potential friend added as a friends_user and set to "pending" for status
# if accepted both entries on the table should be converted to "accepted"
# if declined both entries should be deleted from table
cursor.execute('''CREATE TABLE IF NOT EXISTS friends
                 (username, friends_user, status)''')


#   status can be "saved" "applied" or "deleted"
#   posed parameter is username of job poster
cursor.execute('''CREATE TABLE IF NOT EXISTS app_status
                 (username, title, posted, status)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS applications
                 (username, title, employer, grad_date, start_date, best_fit)''')

