import registration as reg
import database as db
import pages as page
# ---------------------------------JOBS-------------------------------------------------------------


#   True if space, false if no space for jobs
def space_for_job():  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute('SELECT * FROM jobs;')
    if len(curs.fetchall()) < 5:
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


