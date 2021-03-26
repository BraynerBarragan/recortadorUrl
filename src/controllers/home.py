from flask import render_template, request
from src import app
import random
from src.models.url import UrlModel

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
     
        return render_template('index.html')

    url = request.form.get('url')
    urlRecortada = ''
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(4):
        urlRecortada= urlRecortada+letras[random.randrange(26)]
    local = 'http://127.0.0.1:5000/'
    urlModel = UrlModel()
    urlModel.guardar(url, urlRecortada)

    print(url)
    print(urlRecortada)

    return render_template('index.html',url=urlRecortada, local = local)




