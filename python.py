import requests
from bs4 import BeautifulSoup
import openpyxl   
 
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="rating"
sheet.append(["rank","name","year","rating"])

try:
    source=requests.get("https://www.imdb.com/chart/top/").text
    soup=BeautifulSoup(source,"html.parser")
    movies=soup.find('tbody',class_="lister-list")
    each=movies.find_all('tr')

    for movie in each :
        name=movie.find('td',class_='titleColumn').a.text
        rank=movie.find('td',class_="titleColumn").text.split(".")
        rank=rank[0]
        year=movie.find('span',class_="secondaryInfo").text.strip("()")
        rating=movie.find('strong').text
        sheet.append([rank,name,year,rating])
    print("success")
  
except Exception as e:
    print(e)
    
excel.save("rating.xlsx")