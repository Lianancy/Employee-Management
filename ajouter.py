from flask import Flask, render_template, request, jsonify
import mysql.connector
app= Flask(__name__)

connection = mysql.connector.connect(host='localhost', user= 'root', passwd='1234io', database='employe')

@app.route('/')
def index():
    return render_template('ajouter.html')

@app.route("/ajouter", methods=['POST'])
def ajouter():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    date_naissance= request.form.get('date_naissance')
    lieu_naissance= request.form.get('lieu_naissance')
    emploi= request.form.get('emploi')
    num_mat= request.form.get('num_mat')

    mycursor= connection.cursor()
    sql="INSERT INTO employe_info (nom, prenom, date_naissance,lieu_naissance,emploi,num_mat) VALUES (%s, %s, %s, %s, %s, %s)"
    val=(nom, prenom, date_naissance, lieu_naissance,emploi,num_mat)
    mycursor.execute(sql, val)
    connection.commit()
    return render_template('ajouter.html')

if __name__=='__main__':
    app.run(debug=True)


