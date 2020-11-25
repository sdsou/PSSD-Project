
## PSSD-Project

# Project Proposal
--

Proposal: Job Board Notifier

1. **The Big Idea:**
The point of this project is to build an application that can aggregate and return information from across the web to the user. We plan to build a bot that scrubs various job boards based on certain keywords that the user inputs. The bot will log the url, job description, application deadline to generate a report to return the information to the user via email. With this project, the team will explore various automation processes like email and web scraping. At minimum, the program should be able to scrape a job board and return information related to that job to the user by sending an email. Ideally, if successful in all aspects, we would like to polish the interface up and then share the application with CCD for the benefit of the Babson community or create a business out of our service for a small fee from each user.

2. **Learning Goals:**
Given that our team has varied expectations and interests, this project idea is interesting to us all as we can accomplish all of our learning goals through this process. Below is a bulleted list of what we hope to achieve in the 8 weeks.
- **Creating a Robotic Process Automation.** Understanding how it works and it’s implementations outside of this project.
- **Web (HTML/XML) Scraping.** This is a skill we’ve heard in QTM 3 class that can be immensely useful for gathering a lot of data or information quickly and efficiently without exerting too much manual labor of going to various websites, scrolling for information, copying and pasting, etc.
- **Email Automation.** This project will utilize automation in various forms, including emailing users. This is a transferable skill, like many of the other skills, and can have practical uses in our lives.
- **Creating/Using or Integrating a Database in Python.** We will have to have a database integrated in Python to store our data and information. This is something new and will be an expansion on our intermediate/elementary Python skills.
- **Creating a simple API.**
Understanding how the program translates to what the user sees when they are interacting with our program.


3. **Implementation Plan:**
In order to tackle some of the process that we are automating in this project, we plan on using certain libraries. For web-scraping, we can use libraries like BeautifulSoup, Selenium, webbrowser, Requests. In addition to using these library for webscraping, we may also need to learn some very basic HTML in order to use these libraries correctly. While not ideal, one way to store the data scraped from the web would be to save it to a excel sheet using the OpenPyXL library or in a csv file with the csv library. To send emails to the user, we will have to use the smtplib library to login to the smtp/email server and send the email. We were able to gather very basic frameworks for web-scraping, storing the data in a .xlsx or .csv file, and sending emails from the "Automate the Boring Stuff with Python" book, but we will need to modify these frameworks heavily after planning and writing the pseudocode. The best way to prepare would to to write out each phase: web-scraping, creating the database, and sending emails, separately from each other and then slowly integrating the processes.

4. **Project schedule** 

**Week 1:** Create an agenda and set goals for what our project will accomplish and how we are going to meet a need. Share our ideas with others and solicit feedback.

**Week 2:** Start coding by writing Pseudo-code and then translating it into Python Code. The pseudo-code will also help us with writing our comments so that other people can understand it clearly without us having to explain it. Receive initial feedback from Professor Li on our code and make improvements as suggested/needed.

**Week 3:** Continue writing the code and test it. Prepare for Mid-Project Presentation, and be able to explain the code well. At this point we should have attempted scraping job-sites and have decided on how the code is going to scrape the job sites for keywords.

**Week 4:** Present Mid-Project Presentation to class. At this point we would like to check that multiple can use our project without the code resetting each time someone logs in to update their information. Start brainstorming ideas for our project website, and how we can add this experience to our professional portfolio.

**Week 5:** Check the code and create new code if needed to make sure that it can email the jobs found to different emails and that it works for various users. Continue agile development and solicit more feedback from others on what they think could be better. Write-up the documents needed for other people to be able to understand what the code does and what it is used for.

**Week 6:** Launch our project website and check user functionality. Include Big Idea/Goal/Why did we do this?, User instructions/README, Implementation information, Results, Project evolution/narrative, and give credit where credit is due.
Use agile development to continue improving it.

**Week 7:** Work on feedback from other users and improve the website and code as needed/suggested. Work on our pitch and be able to articulate what our project does and how we achieved our goals and what we learned.

**Week 8:** Wrap-up any necessary items and be prepared to present on what we accomplish. Do run-throughs of our presentation and make sure our project website is up to date. Submit the final code.

5. **Collaboration plan:** 

- Meeting using video calls & messaging over Slack
- We will work successfully as a team by keeping respectful and timely communication
- Shoaib will manage the master code, but we intend on having a flat-structure where everyone is expected to contribute equally
- Agile development, working independently but working together to troubleshoot issues & then integrate
- Split up tasks & then integrate them into mastercode 
- We will be pair programming by showing each other the steps & understanding our issues and being able to fix them 

6. **Risks:**
This project when done correctly will be a huge success and has a practical use that can be really helpful for a lot of Babson students as they navigate the internship/job hunt process. Potential risk that we need to mitigate are:
- Correctly writing and implementing the program exactly as we imagine it.
- This project is creating a program that will be an intermediary between a user and multiple  job boards’ information. Thus:
- We need to make sure that we aren’t breaking any potential rules of those job boards
- Do the job boards open for public view or does one need to have an account in order to access it? If so, how do we go about getting information from them with the idea that multiple users will be using this application?
-  We need to correctly store the user and their preferences (keywords) as well as the post entries we have sent them. On that same note, are we going to have a line of code checking entries previously sent to see if there are duplicates of same posts being sent since this would be a compilation of jobs available from multiple job boards

7. **Additional Course Content:**
All of our learning goals mentioned are core to our project and are topics we have not learned yet. These are contents that covered in class will be especially helpful for our project.
