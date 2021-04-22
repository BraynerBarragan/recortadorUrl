from src.config.db import DB
class UsersModel():
    def save(self, name, email, password):
        
        cursor= DB.cursor()

        cursor.execute('insert into users(name, email, password) values(?,?,?)',(name, email, password,))
        cursor.close()

    def consultCheckIn(self, email):
        cursor = DB.cursor()
        cursor.execute('select * from users where email = ?',(email,))
        user = cursor.fetchone()
       
        return user


    def consultLogin(self, email, password):
        cursor = DB.cursor()
        cursor.execute('select * from users where email = ? and password = ?',(email, password,))
        user = cursor.fetchone()
        cursor.close()

        return user

    def insertDate(self, date, email):
        cursor = DB.cursor()
        cursor.execute('update users set date_check = ? where email = ?',(date, email,))
        cursor.close()

    

