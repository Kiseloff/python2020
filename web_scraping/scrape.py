import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
votes = soup.select('.score')

# for link, vote in list(zip(links,votes)):
#     if int(vote.get_text().split()[0]) > 100:
#         print(f'{link.get_text()} -- {vote.get_text()}')

news = [{'title': link.get_text(),
         'href': link.get('href', None),
         'votes': votes[idx].get_text()}
        for idx, link in enumerate(links)
        if int(votes[idx].get_text().split()[0]) > 100
        ]
sorted_news = sorted(news,
                     key=lambda item: int(item['votes'].split()[0]),
                     reverse=True)

pprint(sorted_news)
