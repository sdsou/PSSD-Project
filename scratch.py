import web_scrape as ws

position = "data scientist"
location = "New York"

content = ws.main(position, location)
for key in content:
    print(content[key]["company"])