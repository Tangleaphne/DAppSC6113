from flask import Flask,render_template,request
import sqlite3
import datetime

app=Flask(__name__)

@app.route('/',methods=["get","post"])
def index():
    return render_template('index.html')

@app.route('/role',methods=["get","post"])
def role():
    r = request.form.get("q")
    return render_template('role.html', r=r)

@app.route('/main', methods=['GET', 'POST'])
def main():
    role = request.form.get("role")
    r = request.form.get("q")
    current_time = datetime.datetime.now()
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("insert into user values (?, ?, ?)", (role, r, current_time))
    conn.commit()
    c.close()
    conn.close()
    if role == "user":
        return render_template('main.html', role=role, r=r)
    else:
        return render_template('admin.html', role=role, r=r)

@app.route('/backmain',methods=["get","post"])
def backmain():
    role = request.form.get("role")
    r = request.form.get("q")
    if role == "user":
        return render_template('main.html', role=role, r=r)
    else:
        return render_template('admin.html', role=role, r=r)

@app.route('/viewDB',methods=["get","post"])
def viewDB():
    role = request.form.get("role")
    r = request.form.get("q")
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute("select * from user")
    t = ""
    for row in c:
        t += str(row) + "\n"
    conn.commit()
    c.close()
    conn.close()
    return render_template('viewDB.html', role=role, r=r, t=t)

@app.route('/delDB',methods=["get","post"])
def delDB():
    role = request.form.get("role")
    r = request.form.get("q")
    conn = sqlite3.connect('dapp.db')
    c = conn.cursor()
    c.execute("delete from user")
    conn.commit()
    c.close()
    conn.close()
    return render_template('deleteDB.html', role=role, r=r)

@app.route('/store_money',methods=["get","post"])
def store_money():
    role = request.form.get("role")
    r = request.form.get("q")
    return render_template('store_money.html', role=role, r=r)

@app.route('/transfer_money',methods=["get","post"])
def transfer_money():
    role = request.form.get("role")
    r = request.form.get("q")
    return render_template('transfer_money.html', role=role, r=r)

if __name__=='__main__':
    app.run()
