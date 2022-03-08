from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
start_year, current_year, end_year = 2000, 2000, 2022

def print_constructors_standings():
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


def print_drivers_standings():
    for current_year in range(start_year, end_year):
        print('\n\n\n', current_year)
        url = 'https://www.formula1.com/en/results.html/' + str(current_year) + '/drivers.html'

        content = http.request('GET', url) 
        soup = BeautifulSoup(content.data.decode('utf-8'), 'html.parser')

        table = soup.find('table', 'resultsarchive-table')

        position, driver, nationality, team, points = 0, '', '', '', 0

        for row in table.find_all('tr'):
            if row.find('td'):
                position = row.find('td', 'dark').text
                driver = row.find('span', 'hide-for-tablet').text + ' ' + row.find('span', 'hide-for-mobile').text
                nationality = row.find('td', 'dark semi-bold uppercase').text
                team = row.find('a', 'grey semi-bold uppercase ArchiveLink').text
                points = row.find('td', 'dark bold').text
                print(position, '   | ', driver, '    |  ', nationality, '  |   ', team, ' | ', points)

