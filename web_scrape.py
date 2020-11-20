import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import schedule

"""Source for webscraping indeed: https://www.youtube.com/watch?v=eN_3d4JrL_w"""


def search(position, location):
    """Creates a URL from a job position and a location"""
    position = position.replace(" ", "%20")
    location = location.replace(" ", "%20")
    # salary = salary.replace(",", "%2C")
    template = f"https://www.indeed.com/jobs?q={position}&l={location}"
    return template


# URL = search("data scientist", "New York")

# page = requests.get(URL)
# print(page)
# soup = BeautifulSoup(page.text, "html.parser")
# job_posts = soup.find_all("div", "jobsearch-SerpJobCard")
# # print(len(job_posts))

# job_post = job_posts[0]


def scrub_post(job_post):
    """
    Scrubs the job board and collects the job post information
    """
    atag = job_post.h2.a
    job_title = atag.get("title")
    # print(job_title)
    job_url = "https://www.indeed.com" + atag.get("href")
    # print(job_url)
    company = job_post.find("span", "company").text.strip()
    # print(company)
    job_location = job_post.find("div", "recJobLoc").get("data-rc-loc")
    # print(job_location)
    job_summary = job_post.find("div", "summary").text.strip()
    # print(job_summary)
    post_date = job_post.find("span", "date").text
    # print(post_date)
    today = datetime.today().strftime("%Y-%m-%d")
    # print(today)
    try:
        salary = job_post.find("span", "salaryText").text.strip()
    except AttributeError:
        salary = ""
    result = (
        job_title,
        company,
        job_location,
        salary,
        post_date,
        today,
        job_summary,
        job_url,
    )
    return result


# results = []

# for job in job_posts:
#     result = scrub_post(job)
#     results.append(result)

# print(results)


"""Navigating to the next page"""
# while True:
#     try:
#         URL = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get(
#             "href"
#         )
#     except AttributeError:
#         break
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.text, "html.parser")
#     job_posts = soup.find_all("div", "jobsearch-SerpJobCard")

#     for job in job_posts:
#         result = scrub_post(job)
#         results.append(result)


def main(position, location, sched=False):
    """
    Scrubs job posts based on given position and location.

    Returns: CSV file of information.
    """
    results = []
    URL = search(position, location)

    if sched:
        scheduling(position, location)
    else:
        continue

    while True:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        job_posts = soup.find_all("div", "jobsearch-SerpJobCard")

        for job in job_posts:
            result = scrub_post(job)
            results.append(result)

        try:
            URL = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get(
                "href"
            )
        except AttributeError:
            break

    # Save Job Data
    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "JobTitle",
                "Company",
                "Location",
                "Salary",
                "PostDate",
                "DateRetrieved",
                "Summary",
                "JobUrl",
            ]
        )
        writer.writerows(results)


main("data scientist remote", "New York")
print("Done")


def scheduling(position, location):
    """
    Creating a function for scheduling the webscrapping to occur weekly.
    """
    schedule.every(1).weeks.do(
        main(position, location)
    )  # TODO: not sure if it will read the position, location as variables or not.


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# TODO: Put scheduleing part into HTML possibly, input 1 position, input 2 location

# while True:
#     schedule.run_pending()