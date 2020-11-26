from flask import Flask, render_template, request
from web_scrape import schd_jobs
from email_schedule import send_job_list

app = Flask(__name__)


@app.route("/")
def website():
    return render_template("website.html")


@route("/jobsearch")
def searchform():
    return render_template("page2.html")


@app.route("/searchresults/", methods=["GET", "POST"])
def click_me():
    if request.method == "POST":
        Position = request.form["Position"]
        Location = request.form["Location"]
        Schedule = request.form["Schedule"]
        Email = request.form["Email"]
        content = schd_jobs(Position, Location, Schedule)
        send_job_list(content, Email)
    return render_template(
        "demonstration.html", results=content, position=Position, location=Location
    )
