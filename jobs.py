import registration as reg
import database as db
import pages as page
# ---------------------------------JOBS-------------------------------------------------------------


#   True if space, false if no space for jobs
def space_for_job():  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute('SELECT * FROM jobs;')
    if len(curs.fetchall()) < 10:
        tmpcon.close()
        return True
    else:
        tmpcon.close()
        return False

def post_job_page():
    my_title = input("\nJob title: ")
    my_description = input("\nJob description: ")
    my_employer = input("\nEmployer: ")
    my_location = input("\nJob location: ")
    my_salary = input("\nJob salary: ")
    post_job(my_title, my_description, my_employer, my_location, my_salary)
    page.jobPage()


def post_job(my_title, my_description, my_employer, my_location, my_salary):  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    previous_job_number = fetch_job_numbers()  # track number if items in the table prior adding data
    if previous_job_number < 5:
        tmpcursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?)",
                          (reg.username, my_title, my_description, my_employer,
                           my_location, my_salary))

    tmpcon.commit()
    # for testing purpose and validate that a job has been posted
    data = fetch_job_numbers()  # track number if items in the table after adding data
    if data > previous_job_number:  # comapring data
        print("Job posted")
        tmpcon.close()
        return True
    else:
        print("job not posted")
        tmpcon.close()
        return False


def fetch_job_numbers():  # added function to return the number of items in the jobs table "tested"
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    tmpcursor.execute("SELECT * FROM jobs")
    value = len(tmpcursor.fetchall())
    tmpcon.close()
    return value



def list_jobs(username):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    result = tmpcursor.execute("SELECT * FROM jobs").fetchall()
    
    count = 0
    for i in result:
        #sends username title posted
        tmp = check_job_status(username, i[1], i[0])
        print(str(count) + ". " +  "Title: " + str(i[1]) + "\t Employer: " + str(i[3]) + "\t Location: " + str(i[4]) + "\t Salary: " + str(i[5]) + "\t Description: " + str(i[2]) + "\t Status:"+ tmp)
        count += 1
    
    tmpcon.close()

def check_job_status(username, title, posted):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    #curs = tmpcursor.execute("SELECT * FROM app_status WHERE username = '{}' AND title = '{}' AND posted = '{}'".format(username, title, posted))
    curs = tmpcursor.execute("SELECT * FROM app_status WHERE (username = '{}' AND title = '{}' AND posted = '{}' COLLATE NOCASE)".format(username, title, posted))#, title, posted))
    check = str(curs.fetchone())
    if check == "None":
        tmpcon.close()
        return "None"
    else:
        ret = tmpcursor.execute("SELECT * FROM app_status WHERE (username = '{}' AND title = '{}' AND posted = '{}' COLLATE NOCASE)".format(username, title, posted)).fetchall()
        tmpcon.close()
        #returns the status
        return str(ret[0][3])

def list_jobs_saved(username):
    print("Saved Jobs:")
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    result = tmpcursor.execute("SELECT * FROM app_status WHERE username = '{}' AND status = 'saved' COLLATE NOCASE".format(username)).fetchall()
    
    count = 0
    for i in result:
        jobs_saved = tmpcursor.execute("SELECT * FROM jobs WHERE title = '{}' AND username = '{}' COLLATE NOCASE".format(i[1], i[2])).fetchall()
        print(str(count) + ". " +  "Title: " + str(jobs_saved[0][1]) + "\t Employer: " + str(jobs_saved[0][3]) + "\t Location: " + str(jobs_saved[0][4]) + "\t Salary: " + str(jobs_saved[0][5]) + "\t Description: " + str(jobs_saved[0][2]))
        count += 1
    count = 0



def list_jobs_applied(username):
    print("Applied Jobs:")
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    result = tmpcursor.execute("SELECT * FROM app_status WHERE username = '{}' AND status = 'applied' COLLATE NOCASE".format(username)).fetchall()
    
    count = 0
    for i in result:
        jobs_saved = tmpcursor.execute("SELECT * FROM jobs WHERE title = '{}' AND username = '{}' COLLATE NOCASE".format(i[1], i[2])).fetchall()
        print(str(count) + ". " +  "Title: " + str(jobs_saved[0][1]) + "\t Employer: " + str(jobs_saved[0][3]) + "\t Location: " + str(jobs_saved[0][4]) + "\t Salary: " + str(jobs_saved[0][5]) + "\t Description: " + str(jobs_saved[0][2]))
        count += 1
    count = 0