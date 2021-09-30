import sqlite3
import pytest
import inCollegeApp



def test_is_good_password():
    #testing a good password
    assert inCollegeApp.is_good_password("Killer&06") == True
    #testing all number
    assert inCollegeApp.is_good_password("1233456") == False
    #testing without uppercase
    assert inCollegeApp.is_good_password("peter_012") == False
    #testing without number
    assert inCollegeApp.is_good_password("Password") == False
    #testing too long
    assert inCollegeApp.is_good_password("Nimius_123456") == False
    #testing too short
    assert inCollegeApp.is_good_password("Cat_1") == False

def test_check_for_account():
    assert inCollegeApp.check_for_account("user1", "U1_012345") == True
    assert inCollegeApp.check_for_account("john", "smith") == False
    assert inCollegeApp.check_for_account("user3", "Jorge_06") == False

def test_check_for_username():
    assert inCollegeApp.check_for_username("Jorge") == False
    assert inCollegeApp.check_for_username("user1") == True

def test_space_for_signup():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM users;')
    #getting from database and comparing if less than 5 user.
    if len(curs.fetchall()) < 5:
        assert inCollegeApp.space_for_signup() == True
    else:
        assert inCollegeApp.space_for_signup() == False

#--------------------------------------------------------------------------------------
#                           New Tests
#--------------------------------------------------------------------------------------
def test_space_for_job():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM jobs;')
    #getting from database and comparing if less than 5 jobs.
    if len(curs.fetchall()) < 5:
        assert inCollegeApp.space_for_job() == True
    else:
        assert inCollegeApp.space_for_job() == False

def test_find_friend_account():
    assert inCollegeApp.find_friend_account("Peter", "garas") == True
    assert inCollegeApp.find_friend_account("Will", "Smith") == False

def test_post_job():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM jobs;')
    if len(curs.fetchall()) < 5:
        assert inCollegeApp.post_job('test1', 'test2', 'test3', 'test4', 'test5') == True
    else:
        assert inCollegeApp.post_job('test1', 'test2', 'test3', 'test4', 'test5') == False

def test_fetch_job_numbers():
    conn = sqlite3.connect('inCollege.db')
    cursor = conn.cursor()
    curs = cursor.execute('SELECT * FROM jobs;')
    number = len(cursor.fetchall())
    assert inCollegeApp.fetch_job_numbers() == number

