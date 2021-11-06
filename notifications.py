import database as db
import friends as friend
import registration as reg
from os import system, name
# import sleep to show output for some time period 
from time import sleep

# When the student goes into the jobs section, the system will automatically notify that "You have currently applied for x jobs". 

#a job that a student has applied for has been deleted, then the student will receive a notification that "A job that you applied for has been deleted" along with the name of the job that was deleted. 

#----------------------------------------------------
def numberJobsApplied(username): 
  tmpcon = db.sqlite3.connect('inCollege.db')
  tmpcursor = tmpcon.cursor()
  jobs_applied = tmpcursor.execute(
        "SELECT * FROM app_status WHERE username = '{}' AND status = 'applied' COLLATE NOCASE".format(username)).fetchall()
  applied_count = 0
  for i in jobs_applied:
    applied_count += 1

  tmpcon.close()
  return applied_count

def job_deleted(username):
    tmpcon = db.sqlite3.connect('inCollege.db')
    tmpcursor = tmpcon.cursor()
    curs = tmpcursor.execute("SELECT * FROM app_status WHERE username = '{}' AND status = 'deleted'".format(
        username))  # should username be 'posted' ?
    job_d = curs.fetchone()
    if str(job_d) == "None":
        tmpcon.close()
        print("No jobs that you have applied has been deleted")
    else:
        print("{} \n".format(job_d[0][1]))
        tmpcursor.execute("DELETE FROM app_status WHERE username = '{}' AND status = 'deleted'".format(username))
        tmpcon.commit()
        tmpcon.close()
        return True
  
def notifiTimeJobs(count):
    # for windows 
    notifiPostJob(reg.username)
    print("You have currently applied for {} jobs".format(count)) 
    if job_deleted(reg.username) == True:
      print("This job you have applied for has been deleted.")
    
    sleep(3) 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
     # print out some text 
   
    
#----------------------------------------------------

#If a student has messages from another student, then the system will notify them that "You have messages waiting for you".   

def inboxNotification():
    inbox_list = db.cursor.execute("SELECT * FROM messages WHERE recipient = '{}'".format(reg.username)).fetchall()

    if len(inbox_list):
        return True
    else:
        return False

def notiSystem():
        
    if friend.pending_friend(reg.username) == True:
        print("You have a pending friend request")
    else:
        print("no friend requests :(")

    if inboxNotification():
        print("\nYou have messages waiting for you")
    else:
        print("No new messages")
    
    sleep(3)  
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#When a new job has been posted, the student will be notified "A new job <job title> has been posted." 

def notifiPostJob(username):
  tmpcon = db.sqlite3.connect('inCollege.db')
  tmpcursor = tmpcon.cursor()
  curs = tmpcursor.execute("SELECT * FROM jobs") 
  rows = curs.fetchall()
  for row in rows:
    if username != row[0]:
      print("A new job {} has been posted.".format(row[1]))

  tmpcon.close()

      
  
  

