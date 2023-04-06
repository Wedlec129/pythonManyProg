
#для звука
import pyttsx3
import speech_recognition as sr

#для парчинга
import requests 
from bs4 import BeautifulSoup as BS





def getChesloForhtml(htmlForChislo):
      # Ссылка на нужную страницу
      html = htmlForChislo
    	# Заголовки для передачи вместе с URL
      headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

      full_page = requests.get(html, headers=headers)

      soup = BS(full_page.content, 'html.parser')

      convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2}) #тег классы и какие то значения 

      return( convert[0].text)

def say(watSay):
    #можно говорить
    PC= pyttsx3.init()

   

    PC.say(watSay)


    PC.runAndWait() #начать говорить




ruksDollar=getChesloForhtml("https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=rehc&aqs=chrome.2.69i57j69i59j0l6.3127j1j7&sourceid=chrome&ie=UTF-8");


say("привет "+ruksDollar)



