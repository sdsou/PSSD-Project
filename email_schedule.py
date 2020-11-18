# import schedule
import smtplib
import Emailer as hidden


def web_scrape_job():
    print("A Simple Python Scheduler.")


# schedule.every(2).seconds.do(web_scrape_job)

# while True:
#     schedule.run_pending()


def sendEmail(sender_email, password, to, subject, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com", "587")
        server.starttls()
        server.login(sender_email, password)

        message = f"From: {sender_email}\nTo: {to}\nSubject: {subject}\n\n{msg}"
        print(message)

        server.sendmail(sender_email, to, message)
        server.quit()
        print("Email Sent")
    except Exception as e:
        print(e)
        print("Some Error Occured")


if __name__ == "__main__":
    Email = hidden.email
    Password = hidden.password
    To = "srahaman1@babson.edu"
    Subject = "Testing Email"
    Message = "OMG IT WORKED"
    sendEmail(Email, Password, To, Subject, Message)
