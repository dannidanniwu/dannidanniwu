import requests
from bs4 import BeautifulSoup

def get_citation_count():
    URL = 'https://scholar.google.com/citations?user=ToOwt1kAAAAJ&hl=zh-CN'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation_count = soup.find('div', {'id': 'gsc_rsb_st'}).find_all('td')[1].text
    return citation_count

if __name__ == "__main__":
    count = get_citation_count()
    with open('README.md', 'r') as file:
        content = file.read()
        content = content.replace('CITATION_COUNT_PLACEHOLDER', count)
    with open('README.md', 'w') as file:
        file.write(content)
