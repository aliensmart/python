import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=remote%20junior%20software%20engineer'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# to find just one element we  can use soup.find to find just one one element
result = soup.find(id="resultsBodyContent")
# print(result.prettify())

# to find an element we can use find_all to find all div that have the class name jobsearch-SerpJobCard
jobs = result.find_all('div', class_='jobsearch-SerpJobCard')
# print(jobs[0])

for job in jobs:
    titlesElements = job.find('h2', class_='title')

    # to get attribute of an element
    titleresult = titlesElements.find('a')['title']

    print(titleresult)
    print()
# create requirements.txt ====> python -m pip freeze > requirements.txt
# to install requirements.txt ====> python -m pip install -r requirements.txt