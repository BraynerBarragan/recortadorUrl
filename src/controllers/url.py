from flask import render_template, request, redirect, url_for, session, flash
from src import app
from src.models.url import UrlModel

@app.route('/urls')
def urls():
    if not 'user' in session:
        return redirect(url_for('index'))

    urlModel = UrlModel()
    urls = urlModel.bringUrls(session['user']['id'])
    #print(urls)#
    return render_template('user/list_url.html', urls = urls)

@app.route('/url/edit/<url>', methods=['GET','POST'])
def edit(url):
    if not 'user' in session:
        return redirect(url_for('index'))
    urlModel = UrlModel()
    url = urlModel.traerUrl(url)
    if request.method == 'GET':
        
        #print(url)
        return render_template('user/edit_url.html', url=url)
    
    newUrl = request.form.get('url')
    if newUrl == '':
        print(url)
        flash('No puede quedar el campo vacio','danger')
        return redirect('http://localhost:5000/url/edit/'+url[3])

    urlModel.editUrl(newUrl, url[0])

    flash('Editado correctamente','success')
    return redirect(url_for('urls'))

@app.route('/url/delete/<id>')
def delete(id):
    print(id)
    urlModel = UrlModel()
    urlModel.delete(id)
    return redirect(url_for('urls'))

    