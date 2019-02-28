import csv
import urllib
from bs4 import BeautifulSoup

BASE_URL = 'https://www.weblancer.net/jobs/'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_page_count(html):
    soup = BeautifulSoup(html)
    navigation = soup.find('ul', class_ = 'pagination')
    text = navigation.find_all('a',href = True)[-1]
    last_page = int(text['href'][12:])
    return last_page

def parse(html):
    soup = BeautifulSoup(html)
    table = soup.find('div', class_ = 'container-fluid cols_table show_visited')

    projects = []

    for row in table.find_all('div', class_ = 'row'):
        cols = row.find_all('div')

        projects.append({
            'title': cols[0].h2.text,
            'categories': row.find('div', class_ = 'col-xs-12 text-muted').a.text,
            'price': cols[1].text.strip(),
            'application': cols[2].text.strip().split()[0]
        })
    return projects

def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Проект', 'Категории', 'Цена', 'Заявки'))

        for project in projects:
            writer.writerow((project['title'], project['categories'], project['price'], project['application']))

def main():
    page_count = get_page_count(get_html(BASE_URL))

    print('Всего найдено страниц: %d' % page_count)

    projects = []

    for page in range(1, page_count):
        print('Парсинг %d%%' % ((page / page_count * 100)+1))

        projects.extend(parse(get_html(BASE_URL + '?page=%d' % page)))

    save(projects, 'projects.csv')
if __name__ == '__main__':
    main()
