import requests
import urllib.request
import time
import csv
from datetime import datetime
from bs4 import BeautifulSoup

lottery_page = 'http://www.lnb.gob.pa/numerosjugados.php?tiposorteo=T&ano=%d&meses=%02d&Consultar=Buscar'

for year in range(2011,2020):
    for month in range(1,13):
        print(lottery_page % (year,month))
        response = requests.get(lottery_page % (year,month))
        soup = BeautifulSoup(response.text, 'html.parser')        
        strongs = soup.select("span.style1 > font > strong ", attrs={'class': 'style1'})
        results = []
        for index in range(0,((len(strongs)//8)-1)):    
            row = "" 
            for i in range((index*8)+1,(index*8)+9):
                row = row + strongs[i-1].text + ","        
            results.append(row[:-1])
        for line in results:
            with open('index.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(line.split(','))

        