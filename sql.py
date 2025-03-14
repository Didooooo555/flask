from flask import Flask, render_template,request,url_for,redirect
import mysql.connector
con = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'didar09k',
    database = 'e'
)

app = Flask(__name__)

cursor = con.cursor()
cursor.execute ('''
CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                surname VARCHAR(100),
                class VARCHAR(10),
                message VARCHAR(100),
                date DATE,
                address VARCHAR(100)
)'''
)
cursor.close()

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('proj.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        sql = 'INSERT INTO user (name, surname, class, message, date, address) VALUES(%s,%s,%s,%s,%s,%s)'

        username = request.form['username']
        surname = request.form['surname']
        cla = request.form['class']
        mess = request.form['mess']
        date = request.form['dob']
        ad = request.form['ad']

        cursor = con.cursor()
        cursor.execute(sql, (username, surname, cla, mess, date, ad))
        con.commit()
        cursor.close()
    
        return redirect(url_for('great'))

@app.route('/great')
def great():
    return render_template('great.html')


if __name__ == ('__main__'):
    app.run(debug=True)
cursor.close()
con.close()
