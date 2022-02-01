import time
import requests

def crawler(url):
    print("************ Crawler Started For: {url} **********")
    # Some 5 seconds time consuming task
    response = requests.get(url)
    time.sleep(5)

    while True:
        status_code = (yield)
        if response.status_code==200:
            print(response.text)
        else:
            print("Response not found")
            

web_crawler = crawler("https://www.python.org/")
print("******Web crawler started*********")

next(web_crawler)
print("Started For Next URL")
web_crawler.send("https://www.python.org/downloads/")

web_crawler.close()

