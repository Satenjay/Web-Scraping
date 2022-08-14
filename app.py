from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    url ="https://www.businesstoday.in/latest/economy"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    # print(soup.prettify)
    outerdata=soup.find_all('div', class_="widget-listing",limit=6)
    finalNews = ""
    for data in outerdata:
        news=data.div.div.a["title"]
        finalNews+="\u2022 " + news+"\n"
    # print(finalNews)
    return render_template("index.html",News=finalNews)

