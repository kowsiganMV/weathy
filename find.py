import requests
from bs4 import BeautifulSoup

def weather(city):
  na=city
  req=requests.get(f"https://www.google.com/search?q={na}+weather&rlz=1C1CHBF_enIN1016IN1016&oq=madurai+weather&aqs=chrome..69i57j0i131i433i512j0i512l8.6003j1j4&sourceid=chrome&ie=UTF-8")

  soup=BeautifulSoup(req.content,"html.parser")
  a=soup.get_text()
  b=a[200:500]
  c=b.index("Weather")
  s=b[c:c+200]
  weather=s[7:11]
  day=s.index('day')
  extra=s[day+12:s.index("on weather")]
  time=s[day+3:day+11]
  time=time.replace("\u202f"," ")
  day=s[s.index("°C")+2:day+3]
  li=[weather,extra,time,day]
  return(li)