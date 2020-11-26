# import schedule
import smtplib
import DO_NOT_OPEN as hidden
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import web_scrape as ws
from jinja2 import Environment, FileSystemLoader
import os

# Get tmeplate from file system to load
env = Environment(loader=FileSystemLoader(searchpath="./"))

""" Sources:
https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/#Sending_HTML_email
https://dev.to/carola99/send-an-html-email-template-with-python-and-jinja2-1hd0
https://www.spritecloud.com/creating-and-sending-html-e-mails-with-python/ """


def sendEmail(to, subject, content):
    """Function sends user an email based on contents specified in inputs.
    Source: https://dev.to/bhupesh/a-simple-scheduler-in-python-49di
    """

    try:
        message = MIMEMultipart()
        message["Subject"] = str(subject)
        message["From"] = hidden.email
        message["To"] = to
        message.preamble = "Thank you for using our service!"

        # with open("email_template.html", "r") as f:
        #     html = f.read()
        ### Attach html in the sending of the email
        msgBody = MIMEText(content, "html")
        message.attach(msgBody)
        ### Attach the csv file associated with the search
        ctype, encoding = mimetypes.guess_type("results.csv")
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)

        fp = open("results.csv", "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)

        attachment.add_header(
            "Content-Disposition", "attachment", filename="results.csv"
        )
        message.attach(attachment)

        server = smtplib.SMTP("smtp.gmail.com", "587")
        server.starttls()
        server.login(hidden.email, hidden.password)
        server.sendmail(hidden.email, to, message.as_string())
        server.quit()
        print("Email Sent")
    except Exception as e:
        print(e)
        print("Some Error Occured")


def send_job_list(results, recepient_email):
    To = recepient_email
    Subject = "Fixed Emailer!"
    template = env.get_template("email_template.html")
    output = template.render(
        results=results, position="position", location="ws.location"
    )
    sendEmail(To, Subject, output)


###Combine webscrape w/ scheduler to the emailer

if __name__ == "__main__":
    #    recepient_email = "srahaman1@babson.edu"
    #    send_job_list(recepient_email)
    pass