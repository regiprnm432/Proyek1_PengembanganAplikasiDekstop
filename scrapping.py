from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import urllib.request
import json
import datetime

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.imdb.com/list/ls066095353/")

serieslist = []
i = 1
while i<=100:
    for series in driver.find_elements(By.CLASS_NAME,"lister-item-content"):
         print(series.text.split("\n"))
         for img in series.find_elements(By.TAG_NAME,"img"):
             print(img.get_attribute("src"))
             urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
             i = i+1
             now = datetime.datetime.now()
             serieslist.append(
                 {"No/Judul/Release": series.text.split("\n")[0],
                  "Durasi/Genre": series.text.split("\n")[1],
                  "Rating": series.text.split("\n")[2],
                  "Pemain": series.text.split("\n")[5],
                  "Image": img.get_attribute("src"),
                  "Waktu Scraping": now.strftime("%Y-%m-%d %H:%M:%S")
                 }
             )

hasil_scraping = open("hasilscraping.json","w")
json.dump(serieslist, hasil_scraping, indent = 6)
hasil_scraping.close()
 
driver.quit()

    
       
