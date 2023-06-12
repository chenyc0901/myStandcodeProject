"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features='html.parser')

        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        male_number, female_number, counter = 0, 0, 0

        for tag in tags:
            lists = tag.text.split()

            for i in range(len(lists)):
                if counter/2 < 200:
                    if i % 5 == 2:
                        number = int(lists[i].replace(',', ''))
                        male_number += number
                        counter += 1
                    elif i % 5 == 4:
                        number = int(lists[i].replace(',', ''))
                        female_number += number
                        counter += 1
            print(f'Male Number: {male_number}')
            print(f'Female Number: {female_number}')

if __name__ == '__main__':
    main()
