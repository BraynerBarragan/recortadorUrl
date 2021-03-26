from src.config.db import DB
class UrlModel():
    def guardar(self, url, urlRecortada):
        cursor= DB.cursor()

        cursor.execute('insert into url(url, url_recortada) values(?,?)',(url,urlRecortada,))
        cursor.close()
