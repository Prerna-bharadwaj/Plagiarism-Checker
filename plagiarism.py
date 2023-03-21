from googlesearch import search
from bs4 import BeautifulSoup
import requests

topic = str(input("Topic: "))
query = str(input("Search Query: "))
number_of_searches = int(input("Number of search results: "))
plagiarismCounter = 0

containing_sites = []

for j in search(topic, num=10, stop=10, pause=2):
  res = requests.get(j)
  soup = BeautifulSoup(res.content, "html.parser")
  tag = soup.body.strings
  for string in tag:
    if query in string:
      plagiarismCounter += 1
      containing_sites.append(j)

print(plagiarismCounter)
print("Sites containing Queries:")
if plagiarismCounter > 0:
  for site in containing_sites:
    print(site)
else:
  print("No results found!")
