import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'cadastro'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('Ac1.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  name = request.form['name']
  cpf = request.form['cpf']
  adress = request.form['adress']
  if name and cpf and adress:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_cliente (user_name, user_cpf, user_adress) VALUES (%s, %s, %s)', (name, cpf, adress))
    conn.commit()
  return render_template('Ac1.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select user_name, user_cpf, user_adress from tbl_cliente')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)


