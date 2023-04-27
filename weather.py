from flask import Flask, render_template,request
from find import weather

app=Flask(__name__)


dic={"windly":"https://user-images.githubusercontent.com/85386114/234741944-ebb449b8-c4f3-4287-b4b8-cbefbbdd2f92.png",
     "cloudly":"https://user-images.githubusercontent.com/85386114/234741908-b06c9aa4-0119-4524-9ab3-b4bcc557c63b.jpg",
     "rainy":"https://user-images.githubusercontent.com/85386114/234741930-55cefccb-9a36-4607-b83e-b2d58f1ce0c3.jpg",
     "stromy":"https://user-images.githubusercontent.com/85386114/234741952-a84a8e69-466d-40ba-a8fb-2191e38f4754.png",
     "sunny":"https://user-images.githubusercontent.com/85386114/234741962-2979f9f8-c22c-4479-94f4-2cba87852dd3.png"}

vid={"wind":"https://user-images.githubusercontent.com/85386114/234877117-057cfb02-e3ac-4940-808a-9a93541f520a.mp4",
     "cloud":"https://user-images.githubusercontent.com/85386114/234877161-ad3468a6-8edd-4d13-a9a1-6e5adf397951.mp4",
     "rain":"https://user-images.githubusercontent.com/85386114/234880488-7e91d9dc-3a46-47e7-bfd9-86c7fc62d750.mp4",
     "strom":"https://user-images.githubusercontent.com/85386114/234880770-f027beed-df31-48a0-ae03-b886f6838d29.mp4",
     "sun":"https://user-images.githubusercontent.com/85386114/234880361-bf33fa37-30e4-47ce-aef1-583327ef1119.mp4"}

@app.route("/",methods=['POST','GET'])
def home():
  if request.form.get('action')=='Get':
    try:
      name=request.form['cityname']
      a=weather(name)
      image=""
      video=""
      if "wind" in a[1].lower():
        image+=dic["windly"]
        video+=vid["wind"]
      elif "rain" in a[1].lower():
        image+=dic["rainy"]
        video+=vid["rain"]
      elif "strom" in a[1].lower():
        image+=dic["stromy"]
        video+=vid["strom"]
      elif "sun" in a[1].lower():
        image+=dic["sunny"]
        video+=vid["sun"]
      elif "cloud" in a[1].lower():
        image+=dic["cloudly"]  
        video+=vid["cloud"]   
      else:
        image+="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu1.webp" 
      return render_template('result.html',title='weathy',temp=a[0],which=a[1],time=a[2],day=a[3],namec=name,imag=image,vide=video)
    except:
      return render_template('Notfound.html')
  return render_template('home.html',title='Weathy')

if __name__ =='__main__':  
    app.run(debug = True) 
