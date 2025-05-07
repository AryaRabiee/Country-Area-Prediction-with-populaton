import re
import requests
from bs4 import BeautifulSoup
import mysql.connector
from sklearn import tree
print('connecting to database')
r = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(r.text,'html.parser')
country = soup.find_all('h3', attrs={'class': ['country-name']})
capital = soup.find_all('span', attrs={'class': ['country-capital']})
population = soup.find_all('span', attrs={'class': ['country-population']})
area = soup.find_all('span', attrs={'class': ['country-area']})

cnx = mysql.connector.connect(user='root', password='password', database='databse_name', host='127.0.0.1')
cursor = cnx.cursor()
for i in range(len(country)):
    cursor.execute('INSERT INTO takhmin (name, capital,population,area) VALUES (%s, %s,%s, %s)', 
                   (re.sub(r'\s+', ' ', country[i].text).strip(), 
                    re.sub(r'\s+', ' ', capital[i].text).strip(), 
                    int(re.sub(r'[^\d]', '', population[i].text)), 
                    int(re.sub(r'[^\d]', '', area[i].text))))
print('Data added to database')
cnx.commit()
cursor.close()
cnx.close()



x = []
y = []
mydb = mysql.connector.connect(host='127.0.0.1', database='databse_name', user='root', password='password')
cursor = mydb.cursor()
cursor.execute('SELECT * FROM takhmin')
data = cursor.fetchall()

for line in data:
    x.append([line[2]])  
    y.append(line[3])

cursor.close()
mydb.close()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
jamiat = input()
new_data = [[jamiat]]  
answer = clf.predict(new_data)
print(answer[0])