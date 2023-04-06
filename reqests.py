from email import header
import requests 


r = requests.get('https://appstorrent.ru') #GET запрос
#print(r.history)
r = requests.post('https://appstorrent.ru', data = {'key':'value'})  #POST запрос


jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
url = 'https://httpbin.org/cookies'
#r = requests.get(url, cookies=jar)



r = requests.get('https://httpbin.org/get') #GET запрос
#print(dir(r))
#print(r.content) #html
print(r.text)    #= одинаковы
print(r.json())  #=


header={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
}
r = requests.get('https://httpbin.org/get',headers=header) #GET запрос


data0={
    "name":"alex",
    "birst":"12.12.1212"
}
r = requests.post('https://httpbin.org/get',headers=header, data =data0)  #POST запрос
print(r.json)