#-------------------------------------------------------------------------
# AUTHOR: Michael Wu
# FILENAME: scraper.py
# SPECIFICATION: Breadth-first crawler for the Circular Links section
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 1 hour
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"

# Creating the frontier and seen collections
frontier = [seed]
seen = {seed}


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)


    # Retrieving and parsing the Web page
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")


    # Printing the text contained in the <h1> element
    h1 = soup.find("h1")
    if h1 is not None:
        print(h1.get_text(strip=True))


    # Extracting and processing hyperlinks
    for anchor in soup.find_all("a", href=True):
        link = requests.compat.urljoin(url, anchor["href"])
        link = link.split("#", 1)[0]

        if link.startswith(seed) and link not in seen:
            seen.add(link)
            frontier.append(link)


# Printing all URLs in seen
for url in sorted(seen):
    print(url)
