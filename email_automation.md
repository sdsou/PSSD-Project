Email Automation. This project will utilize automation in various forms, including emailing users. This is a transferable skill, like many of the other skills, and can have practical uses in our lives.


Receive job alert for data scientist postings in the NY area

Notes:
https://www.youtube.com/watch?v=_aeEGiB2mHA 
- download smtp library
  - The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. For details of SMTP and ESMTP operation, consult RFC 821 (Simple Mail Transfer Protocol) and RFC 1869 (SMTP Service Extensions).
  - from smtplib import SMTP
>>> with SMTP("domain.org") as smtp:
...     smtp.noop()
  - import smtplib
  - from email.mine.multipart import MINEMultipart
  - from email.mine.text import MineText
  - from_addr=""
  - to_addr=""
  - msg=MINEMultipart()
  - msg["From"]=from_addr
  - msg["To"]=",".john(to_addr)
  - msg["Subject]="Job alert"
  - body="A new data scientist job in the New York area has been posted!"
  - msg.attach(MINEText(body, "plain"))

https://towardsdatascience.com/email-automation-with-python-72c6da5eef52

https://realpython.com/python-send-email/
- i think if we use option 2 (setting up a local server) that would work for indeed?
  