import requests
from bs4 import BeautifulSoup
import re
import sys
import json
from datetime import datetime, timezone


def add_space_after_EXCLUSIVE(title: str) -> str:
    return re.sub(r"^EXCLUSIVE", r"EXCLUSIVE ", title)


# URL of the website you want to scrape
url = "https://www.dailymail.co.uk/home/index.html"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all headline titles. This is an example and might need adjustment based on the website's structure
    # You might need to inspect the HTML structure and update the class or tag as needed
    headlines = soup.find_all(
        "h2", class_="linkro-darkred"
    )  # This is a placeholder class; adjust it based on actual website structure

else:
    print("Failed to retrieve the webpage")
    sys.exit(0)

# Get the current timestamp in UTC
now = datetime.now(timezone.utc)

# Format the timestamp in ISO 8601 format with full time zone information
iso_8601_string = now.isoformat()

headlines_dict = {}
headlines_dict[iso_8601_string] = [
    add_space_after_EXCLUSIVE(headline.text.strip()) for headline in headlines
]

with open("daily_mail_headlines.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(headlines_dict, ensure_ascii=False))
