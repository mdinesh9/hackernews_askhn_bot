import csv
import glob
import re
from html.parser import HTMLParser

import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests.exceptions import SSLError, ConnectionError, Timeout, \
     HTTPError, ConnectTimeout, ReadTimeout, InvalidSchema, RetryError
from simplejson.errors import JSONDecodeError

    
already_scraped = pd.read_csv("./data/processed/training_data copy.csv")["id"].values.tolist()
already_scraped = [int(no) for no in already_scraped]

output = csv.writer(open("./data/processed/training_data.csv", "w"))
output.writerow(["id","title", "title_content", "comment"])

def get_json(url):
    try:
        return requests.get(url).json()
    except (SSLError, ConnectionError, Timeout, \
     HTTPError, ConnectTimeout, ReadTimeout, InvalidSchema, \
     RetryError, JSONDecodeError) as e:
        print("Invalid")
        return None

def clean(text):
    if isinstance(text, str):    
        h = HTMLParser()
        cleaned_text = h.unescape(text)

        soup = BeautifulSoup(cleaned_text)
        return soup.get_text().replace("Ask HN: ","")\
            .replace("?"," ").strip()
    return text

def construct_url(id):
    return "https://hacker-news.firebaseio.com/v0/item/" + str(id) + ".json"

def validation(text):
    checks = ["who is hiring","who is firing"]
    if all([check not in text.lower() for check in checks]):
        return True
    return False

def comments_validation(kids):
    if kids:
        if len(kids) > 1:
            return True
        print("Invalid")
        return False
    print("Invalid")
    return False

count = 1

def run():
    """
    1. Opens each hn thread
    2. Reads the first comment
    3. Dumps the hn title, hn title content and first comment to a csv file
    """
    global count
    hn_threads = glob.glob("./data/raw/*.csv")

    for thread in hn_threads:
        data = pd.read_csv(thread)
        data = data[data["score"] > 5]
        data = data[~data["id"].isin(already_scraped)] # remove already scraped


        # loop through each row from input csv
        for story_id, story_score, story_title, story_content in zip(data["id"], \
            data["score"], data["title"], data["text"]):

            if int(story_id) not in already_scraped:

                story_title = clean(story_title)
                story_content = clean(story_content)

                # fetch title and first comment
                story_url = construct_url(story_id)
                story_json = get_json(story_url)
                
                # if json return is not None
                if story_json:
                    kids = story_json.get("kids")
                    
                    # custom validation checks
                    if comments_validation(kids) and story_score > 5 and \
                        validation(story_title):

                        first_commentid = kids[0]
                        comments_url = construct_url(first_commentid)
                        comment_json = get_json(comments_url)

                        if comment_json:
                            comment_text = comment_json.get("text")

                            if comment_text:
                                comment = clean(comment_text)

                                count += 1
                                print(count)

                                # write title, title content and comment to a csv file
                                output.writerow([story_id, story_title, story_content, comment])
            else:
                print("Already exists")


if __name__ == "__main__":
    run()

