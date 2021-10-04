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


# make this relatable to the friends
# cursor.execute('''CREATE TABLE IF NOT EXISTS friends
#                 (username)''')

