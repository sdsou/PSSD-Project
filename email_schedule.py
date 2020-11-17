import schedule


def web_scrape_job():
    print("A Simple Python Scheduler.")


schedule.every(2).seconds.do(web_scrape_job)

while True:
    schedule.run_pending()
