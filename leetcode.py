import requests
from bs4 import BeautifulSoup
import openpyxl

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title="leetcode"
sheet.append(["no","problem","acceptance","difficult"])


source=requests.get("https://leetcode.com/problemset/all/").text
soup=BeautifulSoup(source,'html.parser')

item=soup.find('div',class_='inline-block min-w-full')

each=item.find_all('div',role='row')

for problem in each[1:]:
    s=problem.a.text
    name=s.split('.')
    name=name[-1]
    difficult=problem.text.split("%")
    difficult=difficult[-1]
    no=problem.text.split(".")
    number=no[0]
    acceptance=""
    no[-1]="."+no[-1]
    n="".join(no[1:])

    for x in n:
        if ord(x)>=49 and ord(x)<=58 :
            acceptance+=x
        if x==".":
            acceptance+="."
        if x=="%":
            acceptance+="%"
            break
    sum_name=name
    sheet.append([number,sum_name,acceptance,difficult])
    
wb.save('leetcode.xlsx')
print("success")

    
    