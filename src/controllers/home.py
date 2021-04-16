from flask import render_template, request, redirect, url_for
from src import app
import random
from src.models.url import UrlModel
#urlRecortada = ''
@app.route('/', methods=['GET','POST'])
def index():
    
    #urlModel.eliminar()
    if request.method == 'GET':
        
        return render_template('index.html')
   
    url = request.form.get('url')
    urlRecortada = ''
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

    for i in range(4):
        urlRecortada= urlRecortada+letras[random.randrange(36)]
    
    local = 'http://127.0.0.1:5000/'
    urlModel = UrlModel()
   #urlModel.eliminar()
    urlModel.guardar(url, urlRecortada)
    print(url)
    print(urlRecortada)

    return render_template('index.html',url=urlRecortada, local = local)

@app.route('/<urlRecortada>')
def link(urlRecortada):
    urlModel = UrlModel()
    lin = []
    lin = urlModel.traerUrl(urlRecortada)
    if lin is not None:
        lin = lin[0]
    #urlModel.eliminar()
    # print(urlRecortada)
    return redirect(lin)
