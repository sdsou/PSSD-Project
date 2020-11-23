# import schedule
import smtplib
import DO_NOT_OPEN as hidden
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import web_scrape as ws


def sendEmail(to, subject, msg):
    """Function sends user an email based on contents specified in inputs.
    Source: https://dev.to/bhupesh/a-simple-scheduler-in-python-49di
    """

    try:
        server = smtplib.SMTP("smtp.gmail.com", "587")
        server.starttls()
        server.login(hidden.email, hidden.password)

        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = hidden.email
        message["To"] = to

        message.attach(MIMEText(msg, "html"))
        msgBody = msg.as_string()  ########### Uncalled Variable

        server.sendmail(hidden.email, to, message)
        server.quit()
        print("Email Sent")
    except Exception as e:
        print(e)
        print("Some Error Occured")


def send_job_list(recepient_email):
    To = recepient_email
    Subject = "Testing Email"
    template = env.get_template(
        "email.html"
    )  # Need To Figure out how to get the email template
    Message = template.render(ws.results)  # and then how to render it
    sendEmail(To, Subject, Message)


###Combine webscrape w/ scheduler to the emailer

if __name__ == "__main__":
    recepient_email = "srahaman1@babson.edu"
    send_job_list(recepient_email)