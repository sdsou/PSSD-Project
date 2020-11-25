from flask import Flask, render_template, request
import web_scrape as ws
import email_schedule as es

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def click_me():
    if request.method == "POST":
        Position = request.form["Position"]
        Location = request.form["Location"]
        content = ws.schd_jobs(Position, Location, False)
    return render_template(
        "demonstration.html", results=results, position=Position, location=Location
    )
