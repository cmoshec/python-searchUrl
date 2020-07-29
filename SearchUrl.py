from bs4 import BeautifulSoup
import requests
import re
import csv
import random
from time import sleep

#open here the file UrlSearchList.csv, copy the names to the file , remove any spaces, and save. the best way is to prepare the list in a csv file in excel and to copy the list and paste to a mail in gmail the results of the search will be exported to UrlList.csv
#turn all letters into lower case

url=input("insert url: ")

print('Searching...','\n')
pubNum=[]
with open('UrlSearchList.csv','r') as csv_file_read:
    csv_reader=csv.reader(csv_file_read)
    for line in csv_reader:
         pubNum.append(line[0].strip().lower())
         print(line[0])
         
csv_file=open('UrlList.csv','w')
csv_writer=csv.writer(csv_file)


#url='https://www.algatech.com/'

r = requests.get(url)
data = r.text

soup = BeautifulSoup(data,'html.parser')
tbody = soup.get_text().lower()         

i=0
print('\n')

for pn in pubNum:


    x=pubNum[i]
    i=i+1
    if x in tbody:
       print(x,' - found')
       found='found'
       pos=tbody.index(x)
       sent=tbody[pos:pos+50]
       print(sent,'\n')
    else:
       print(x,' - not found')
       found='not found'
    csv_writer.writerow([x,found])
    
print('\n','exported to UrlList.csv')