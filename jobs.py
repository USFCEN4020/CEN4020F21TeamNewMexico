import registration as reg
import database as db
import pages as page
import menus as menu
import prev_page as pv
import api


# ---------------------------------JOBS-------------------------------------------------------------

def jobSelectPage(jobs):
    if page.pagesVisited[-1] != "jobsSelect":
        page.pagesVisited.append("jobsSelect")
    
    while(True):
        #print job details
        print("\n1. Apply for job"
            "\n2. Save job"
            "\n3. Unsave job"
            "\n4. Go back")
        selection = menu.user_input(4)
        if selection == 1:
            apply_job(jobs, reg.username)
        elif selection == 2:
            save_job(jobs, reg.username, True)      
        elif selection == 3:
            save_job(jobs, reg.username, False)        
        elif selection == 4:
            pv.previous()
        break

def jobPage():
    if page.pagesVisited[-1] != "jobs":
        page.pagesVisited.append("jobs")
    api.output_users()
    api.output_training()
    api.output_appliedJobs()
    api.output_savedJobs()
    api.output_profiles()
    while(True):
        print("\n1. Post a job"
            "\n2. List all jobs"
            "\n3. List jobs applied to"
            "\n4. List saved jobs"
            "\n5. Delete a job"
            "\n6. Go back")

        selection = menu.user_input(6)

        if selection == 1:
            post_job_page()
        elif selection == 2:
            select = list_jobs(reg.username)
            if select != 0:
                jobSelectPage(select)
        elif selection == 3:
            select = list_jobs_applied(reg.username)
            if select != 0:
                jobSelectPage(select)
        elif selection == 4:
            select = list_jobs_saved(reg.username)
            if select != 0:
                jobSelectPage(select)
        elif selection == 5:
            select = delete_job(reg.username)
        elif selection == 6:
            pv.previous()
            break


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
    jobPage()


def post_job(my_title, my_description, my_employer, my_location, my_salary, user = None, request = False):  # tested
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    previous_job_number = fetch_job_numbers()  # track number if items in the table prior adding data
    #if previous_job_number < 5:
    #    tmpcursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?)",
    #                      (reg.username, my_title, my_description, my_employer,
    #                       my_location, my_salary))
    if previous_job_number <= 10 and request:
        tmpcursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?)",
                          (user, my_title, my_description, my_employer,
                           my_location, my_salary))
    elif previous_job_number <= 10:
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


# takes in current username, returns the job selected, or returns "0" if wishing to go back
def list_jobs(username):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    jobs = tmpcursor.execute("SELECT * FROM jobs").fetchall()
    store_list = []
    count = 1
    print("0. Go Back")
    for i in jobs:
        # sends username title posted
        store_list.append(i)
        tmp = check_job_status(username, i[1], i[0])
        print(str(count) + ". " + "Title: " + str(i[1]) + "\t Employer: " + str(i[3]) + "\t Location: " + str(
            i[4]) + "\t Salary: " + str(i[5]) + "\t Description: " + str(i[2]) + "\t Status:" + tmp)
        count += 1

    tmpcon.close()

    selection = menu.user_input(count - 1)
    if (selection == 0):
        return 0
    return store_list[selection - 1]


def check_job_status(username, title, posted):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    # curs = tmpcursor.execute("SELECT * FROM app_status WHERE username = '{}' AND title = '{}' AND posted = '{
    # }'".format(username, title, posted))
    curs = tmpcursor.execute(
        "SELECT * FROM app_status WHERE (username = '{}' AND title = '{}' AND posted = '{}' COLLATE NOCASE)".format(
            username, title, posted))  # , title, posted))
    check = str(curs.fetchone())
    if check == "None":
        tmpcon.close()
        return "None"
    else:
        ret = tmpcursor.execute(
            "SELECT * FROM app_status WHERE (username = '{}' AND title = '{}' AND posted = '{}' COLLATE NOCASE)".format(
                username, title, posted)).fetchall()
        tmpcon.close()
        # returns the status
        return str(ret[0][3])


# not working yet
def list_jobs_saved(username):
    print("Saved Jobs:")
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    jobs = tmpcursor.execute(
        "SELECT * FROM app_status WHERE username = '{}' AND status = 'saved' COLLATE NOCASE".format(
            username)).fetchall()
    store_list = []
    count = 1
    print("0. Go Back")
    for i in jobs:
        # sends username title posted
        jobs_saved = tmpcursor.execute(
            "SELECT * FROM jobs WHERE title = '{}' AND username = '{}' COLLATE NOCASE".format(i[1], i[2])).fetchall()
        store_list.append(jobs_saved[0])
        print(str(count) + ". " + "Title: " + str(jobs_saved[0][1]) + "\t Employer: " + str(
            jobs_saved[0][3]) + "\t Location: " + str(jobs_saved[0][4]) + "\t Salary: " + str(
            jobs_saved[0][5]) + "\t Description: " + str(jobs_saved[0][2]))
        count += 1

    tmpcon.close()
    selection = menu.user_input(count - 1)
    if (selection == 0):
        return 0

    return store_list[selection - 1]


# not working yet
def list_jobs_applied(username):
    print("Applied Jobs:")
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    jobs = tmpcursor.execute(
        "SELECT * FROM app_status WHERE username = '{}' AND status = 'applied' COLLATE NOCASE".format(
            username)).fetchall()
    store_list = []
    count = 1
    print("0. Go Back")
    for i in jobs:
        # sends username title posted
        jobs_saved = tmpcursor.execute(
            "SELECT * FROM jobs WHERE title = '{}' AND username = '{}' COLLATE NOCASE".format(i[1], i[2])).fetchall()
        store_list.append(jobs_saved[0])
        print(str(count) + ". " + "Title: " + str(jobs_saved[0][1]) + "\t Employer: " + str(
            jobs_saved[0][3]) + "\t Location: " + str(jobs_saved[0][4]) + "\t Salary: " + str(
            jobs_saved[0][5]) + "\t Description: " + str(jobs_saved[0][2]))
        count += 1

    tmpcon.close()
    selection = menu.user_input(count - 1)
    if selection == 0:
        return 0

    return store_list[selection - 1]


# jobs (username, title, description, employer, location, salary)
# app_status (username, title, posted, status)
# applications (username, title, employer, grad_date, date_start, best_fit)
def apply_job(job, current_user):
    print("Apply for Jobs:")
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    # checks if user is the poster
    if str(job[0]) == str(current_user):
        print("You posted this job, you cannot apply.")
        return

    # checks if already applied, already saved, or neither. The if saved or neither itll apply  them.
    status = str(check_job_status(current_user, job[1], job[0]))
    if status == "applied":
        print("Already applied")
        return
    elif status == "saved":
        tmpcursor.execute(
            "UPDATE app_status SET status = 'applied' WHERE username = '{}' AND title = '{}' AND status = 'saved'".format(
                current_user, job[1]))
    # the none category means hasn't applied yet or saved yet
    else:
        tmpcursor.execute(
            "INSERT INTO app_status VALUES ('{}', '{}', '{}', 'applied')".format(current_user, job[1], job[0]))

    # inputs for the applications table
    grad_d = input("Give your graduation date in the form of mm/dd/yyyy\n")
    start_d = input("Give the date you can begin work in the form of mm/dd/yyyy\n")
    parag = input("Explain why you are the best fit for this position.\n")

    # uploads application to table
    tmpcursor.execute(
        "INSERT INTO applications VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(current_user, job[1], job[3],
                                                                                      grad_d, start_d, parag))
    tmpcon.commit()

def write_jobs():
    with open('MyCollege_jobs.txt', 'w') as file:
        tmpcon = db.sqlite3.connect('inCollege.db')
        tmpcursor = tmpcon.cursor()
        jobs = tmpcursor.execute('SELECT * FROM jobs').fetchall()
        for i in range(0, len(jobs)):
            file.write("{}\n{}\n{}\n{}\n{}\n=====\n".format(jobs[i][1], jobs[i][2], jobs[i][3], jobs[i][4], jobs[i][5]))


def job_deleted(username):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM app_status WHERE username = '{}' AND status = 'deleted'".format(
        username))  # should username be 'posted' ?
    if str(curs.fetchone()) == "None":
        tmpcon.close()
        return False
    else:
        tmpcursor.execute("DELETE FROM app_status WHERE username = '{}' AND status = 'deleted'".format(username))
        tmpcon.commit()
        tmpcon.close()
        return True


# save true = save, save false = unsave
def save_job(job, current_user, save):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    # checks if already applied, already saved, or neither. The if saved or neither it'll apply  them.
    status = str(check_job_status(current_user, job[1], job[0]))
    if status == "applied":
        print("Already applied")
        return
    elif status == "saved" and save == True:
        print("Already saved job")
        return
    elif status == "saved" and save == False:
        print("Job Unsaved")
        tmpcursor.execute(
            "DELETE FROM app_status WHERE username = '{}' AND title = '{}' AND posted = '{}' AND status = 'saved'".format(
                current_user, job[1], job[0]))
    elif status == "none" and save == False:
        print("Cannot unsave a job you have not saved")
    # the none category means hasn't applied yet or saved yet
    else:
        print("Job Saved")
        tmpcursor.execute(
            "INSERT INTO app_status VALUES ('{}', '{}', '{}', 'saved')".format(current_user, job[1], job[0]))
    tmpcon.commit()
    tmpcon.close()
    return


def delete_job(username):
    #   lists jobs posted by user username
    #   prompts user for job to delete
    #   deletes job from tables
    print("Your Posted Jobs:")
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()

    #   jobs posted by username
    jobs = tmpcursor.execute("SELECT * FROM jobs WHERE username = '{}'".format(username)).fetchall()
    store_list = []
    count = 1
    print("0. Go Back")

    # list all jobs the user posted posted, store them
    for i in jobs:
        store_list.append(i)
        print(str(count) + ". " + "Title: " + str(i[1]) + "\t Employer: " + str(
            i[3]) + "\t Location: " + str(i[4]) + "\t Salary: " + str(
            i[5]) + "\t Description: " + str(i[2]))
        count += 1

    #   prompt selection from user
    selection = menu.user_input(count - 1)
    if selection == 0:
        tmpcon.commit()
        tmpcon.close()
        return 0

    deleted = store_list[selection - 1]
    print(deleted)
    tmpcursor.execute("DELETE FROM jobs WHERE username = '{}' AND title = '{}' AND employer = '{}' AND location = '{}'".format(username, deleted[1], deleted[3], deleted[4]))

    apps = tmpcursor.execute("SELECT * FROM app_status WHERE posted = '{}' AND title = '{}'".format(username, deleted[1])).fetchall()

    for j in apps:
        tmpcursor.execute("UPDATE app_status SET status = 'deleted' WHERE username = '{}' AND title = '{}' AND posted = '{}'".format(j[0], j[1], username))

    tmpcon.commit()
    tmpcon.close()