import sqlite3 
import pytest
import epic_3
from io import StringIO

'''For testing purpose the Database been fill with 3 users
table users
 FirstName  LastName  username  pssw      friends
    Jon  |  Snow  |  user1 | Password_1 | 0
    Gon  | Freecs |  user2 | Password_2 | 0
    Lisa | Simpson| user3  | Password_3 | 0

 for testing if exceeds more than 5, simply two more user can be added in the dashboard

since an user input is needed for testing the -s flag is implemented
ex:  

How to test our code:
> pytest -vv -s .\test_epic_3.py
> 7 (exit)

All tests should be executed and passed.
 '''

def test_is_good_password():
    #testing a good password
    assert epic_3.is_good_password("Killer&06") == True
    #testing all number
    assert epic_3.is_good_password("1233456") == False
    #testing without uppercase
    assert epic_3.is_good_password("peter_012") == False
    #testing without number
    assert epic_3.is_good_password("Password") == False
    #testing too long
    assert epic_3.is_good_password("Nimius_123456") == False
    #testing too short
    assert epic_3.is_good_password("Cat_1") == False

def test_check_for_account():
    assert epic_3.check_for_account("user1", "Password_1") == True
    assert epic_3.check_for_account("john", "smith") == False
    assert epic_3.check_for_account("user3", "Jorge_06") == False

def test_check_for_username():
    assert epic_3.check_for_username("Jorge") == False
    assert epic_3.check_for_username("user1") == True

def test_space_for_signup():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM users;')
    #getting from database and comparing if less than 5 user.
    if len(curs.fetchall()) < 5:
        assert epic_3.space_for_signup() == True
    else:
        assert epic_3.space_for_signup() == False

#--------------------------------------------------------------------------------------
#                           Week 2 Tests
#--------------------------------------------------------------------------------------
def test_space_for_job():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM jobs;')
    #getting from database and comparing if less than 5 jobs.
    if len(curs.fetchall()) < 5:
        assert epic_3.space_for_job() == True
    else:
        assert epic_3.space_for_job() == False

def test_find_friend_account():
    assert epic_3.find_friend_account("Jon", "Snow") == True
    assert epic_3.find_friend_account("Will", "Smith") == False

def test_post_job():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM jobs;')
    if len(curs.fetchall()) < 5:
        assert epic_3.post_job('test1', 'test2', 'test3', 'test4', 'test5') == True
    else:
        assert epic_3.post_job('test1', 'test2', 'test3', 'test4', 'test5') == False

def test_fetch_job_numbers():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM jobs;')
    number = len(cursor.fetchall())
    assert epic_3.fetch_job_numbers() == number

#--------------------------------------------------------------------------------------
#                           Week 3 Tests
#--------------------------------------------------------------------------------------

def test_on_off_mail(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))
    assert epic_3.on_off_mail() == "ON"
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))
    assert epic_3.on_off_mail() == "OFF"

def test_on_off_sms(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))
    assert epic_3.on_off_sms() == "ON"
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))
    assert epic_3.on_off_sms() == "OFF"
    
def test_on_off_ads(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))
    assert epic_3.on_off_ads() == "ON"
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))
    assert epic_3.on_off_ads() == "OFF"

def test_language(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))
    assert epic_3.language() == "English"
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))
    assert epic_3.language() == "Spanish"
