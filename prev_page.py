import pages as page
import jobs
import profile as pf
def previous():
    # pull up previous
    page.pagesVisited.pop()
    # last element in list
    print(page.pagesVisited[-1] + "\n")

    if page.pagesVisited[-1] == "homepage":
        page.homepage()

    if page.pagesVisited[-1] == "mainpage":
        page.mainPage()

    elif page.pagesVisited[-1] == "skills":
        page.skillsPage()

    elif page.pagesVisited[-1] == "python":
        page.pythonPage()

    elif page.pagesVisited[-1] == "java":
        page.javaPage()

    elif page.pagesVisited[-1] == "c":
        page.cPage()

    elif page.pagesVisited[-1] == "c++":
        page.cppPage()

    elif page.pagesVisited[-1] == "ruby":
        page.rubyPage()

    elif page.pagesVisited[-1] == "jobs":
        page.jobPage()

    elif page.pagesVisited[-1] == "jobsSelect":
        page.jobSelectPage()

    elif page.pagesVisited[-1] == "post a job":
        jobs.post_job_page()

    elif page.pagesVisited[-1] == "friends":
        page.friendsPage()

    elif page.pagesVisited[-1] == "findfriends":
        page.findfriendsPage()

    elif page.pagesVisited[-1] == "useful links":
        page.usefulLinksPage()

    elif page.pagesVisited[-1] == "important links":
        page.importantLinksPage()

    elif page.pagesVisited[-1] == "general":
        page.generalPage()

    elif page.pagesVisited[-1] == "browse in college":
        page.browseInCollegePage()

    elif page.pagesVisited[-1] == "business solutions":
        page.businessSolutionsPage()

    elif page.pagesVisited[-1] == "directories":
        page.directories()

    elif page.pagesVisited[-1] == "copyright notice":
        page.copyrightNotice()

    elif page.pagesVisited[-1] == "about":
        page.about()

    elif page.pagesVisited[-1] == "accessibility":
        page.accessibility()

    elif page.pagesVisited[-1] == "user agreement":
        page.userAgreement()

    elif page.pagesVisited[-1] == "privacy policy":
        page.privacyPolicy()

    elif page.pagesVisited[-1] == "cookie policy":
        page.cookiePolicy()

    elif page.pagesVisited[-1] == "copyright policy":
        page.copyRightPolicy()

    elif page.pagesVisited[-1] == "brand policy":
        page.brandPolicy()

    elif page.pagesVisited[-1] == "guest controls":
        page.guestControls()

    elif page.pagesVisited[-1] == "help center":
        page.helpCenterPage()

    elif page.pagesVisited[-1] == "press":
        page.pressPage()

    elif page.pagesVisited[-1] == "blog":
        page.BlogPage()

    elif page.pagesVisited[-1] == "carrier":
        page.carrierPage()

    elif page.pagesVisited[-1] == "developer":
        page.devPage()

    elif page.pagesVisited[-1] == "profile":
        page.profilePage()
    
    # elif page.pagesVisited[-1] == "aboutProfile":
    #     page.profilePage()

    # elif page.pagesVisited[-1] == "experience":
    #     page.profilePage()
    # elif page.pagesVisited[-1] == " view-profile":
    #      pf.viewProfile()
       