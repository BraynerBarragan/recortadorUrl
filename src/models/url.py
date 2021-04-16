from src.config.db import DB
class UrlModel():
    def guardar(self, url, urlRecortada):
        cursor= DB.cursor()

        cursor.execute('insert into url(url, url_recortada) values(?,?)',(url,urlRecortada,))
        cursor.close()
    
    def eliminar(self):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM url WHERE id > 0')
        cursor.close()

    def traerUrl(self, url):
        cursor = DB.cursor()
        cursor.execute('select url from url where url_recortada = ?',(url,))
        urlo = cursor.fetchone()
        cursor.close()
        return urlo


