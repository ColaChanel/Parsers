import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

site = f'http://knowyourmeme.com/memes/all/page/1'

response = requests.get(site, headers={'User-Agent': UserAgent().chrome})
for key, value in response.request.headers.items():
    print(key+": "+value)
print(response)
# soup = BeautifulSoup(response.text, 'html.parser')
# img_tags = soup.find_all('img')

# urls = [img['src'] for img in img_tags]
# print('working')

# for url in urls:
#     filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
#     if not filename:
#          print("Regex didn't match with the url: {}".format(url))
#          continue
#     with open(filename.group(1), 'wb') as f:
#         if 'http' not in url:
#             # sometimes an image source can be relative 
#             # if it is provide the base url which also happens 
#             # to be the site variable atm. 
#             url = '{}{}'.format(site, url)
#         response = requests.get(url)
#         f.write(response.content)