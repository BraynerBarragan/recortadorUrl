from src.config.db import DB
class UrlModel():
    def guardar(self, url, userId, urlRecortada):
        cursor= DB.cursor()

        cursor.execute('insert into url(url, user_id, url_recortada) values(?,?,?)',(url, userId, urlRecortada,))
        cursor.close()
    
    def eliminar(self):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM url WHERE id > 0')
        cursor.close()

    def traerUrl(self, url):
        cursor = DB.cursor()
        cursor.execute('select * from url where url_recortada = ?',(url,))
        urlo = cursor.fetchone()
        cursor.close()
        return urlo

    def bringUrls(self, userId):
        cursor = DB.cursor()
        cursor.execute('select * from url where user_id = ?',(userId,))
        urls = cursor.fetchall()
        cursor.close()
        return urls

    def editUrl(self,url, id):
        cursor = DB.cursor()
        cursor.execute('update url set url = ? where id = ?',(url, id,))
        cursor.close()
    
    def delete(self, id):
        cursor = DB.cursor()
        cursor.execute('delete from url where id = ?',(id,))
        cursor.close
