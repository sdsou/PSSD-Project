# import schedule
import smtplib
import Emailer as hidden


def sendEmail(sender_email, password, to, subject, msg):
    """Function sends user an email based on contents specified in inputs.
    Source: https://dev.to/bhupesh/a-simple-scheduler-in-python-49di
    """

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
