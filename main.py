from flask import Flask,request,render_template
from flaskext.mysql import MySQL
mysql=MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = '0608'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn=mysql.connect()
cursor=conn.cursor()

#cursor.execute('CREATE TABLE userlist(name varchar(255),message varchar(255))')

@app.route('/')
def main():
    #cursor.execute('SELECT * FROM userlist ')
    #data = cursor.fetchone()
    #cursor.close()

    #return data.message
    cursor.execute('SELECT * FROM userlist ')
    data = cursor.fetchall()

    return render_template("template.html",data=data)

@app.route("/input",methods=["POST"])
def message():
    user_name = request.form.get('UserName')
    content = request.form.get('Content')
    
    cursor.execute('INSERT INTO userlist(name,message) VALUES (%s, %s) ',(user_name,content))
    conn.commit()

    cursor.execute('SELECT * FROM userlist ')
    data = cursor.fetchall()

    #return render_template("messages.html",User=user_name,Con=content)
    #return render_template("dot.html",data=data)
    return render_template("template.html",data=data)

app.run(port=1271)