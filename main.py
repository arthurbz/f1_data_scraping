from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
start_year, current_year, end_year = 2000, 2000, 2022

for current_year in range(start_year, end_year):
    print('\n\n\n', current_year)
    url = 'https://www.formula1.com/en/results.html/' + str(current_year) + '/team.html'

    content = http.request('GET', url) 
    soup = BeautifulSoup(content.data.decode('utf-8'), 'html.parser')

    table = soup.find('table', 'resultsarchive-table')

    position, team, points = 0, '', 0

    for row in table.find_all('tr'):
        if row.find('td', 'dark'):
            position = row.find('td', 'dark').text
            team = row.find('a').text
            points = row.find('td', 'dark bold').text
            print(position, team, points)
