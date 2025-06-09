from flask import Flask
from flask import render_template, request, url_for ,redirect

from flask_sqlalchemy import SQLAlchemy

#Istanzio l'app flask
app = Flask(__name__)

#Creiamo il db sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///utenti.db'
db = SQLAlchemy(app) #creo un istanza di sqlalchemy

class Utente(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(80),nullable= False)  #Nullable indica che il dato è obbligatorio
    cognome = db.Column(db.String(80),nullable= True)
    email = db.Column(db.String(80), nullable=False)
    
#per creare il file del database 
with app.app_context():
    db.create_all() #crea tutte le tabelle definite nei modelli


#Definiamo la route per la homepage, ti mette il rete la pagina sotto la rotta specificata (Es: '/about')
@app.route('/')
def home():
    return render_template('index.html', titolo= "Benvenuto", messaggio="Questo è un template html")
#Se compili usando python app-prova.py
#ti darà l'indirizzo che puoi accedere con ctrl + click

#la si può accedere facendo /about
@app.route('/about')
def about():
    return'Pagina About'

#puoi passargli variabili usando curl
@app.route('/user/<nome>')
def user(nome):
    return render_template("index.html", titolo="Profilo", messaggio=f"Ciao{nome}!")

#pagina di login con il form
@app.route('/login', methods= ['GET', 'POST'])
def login():
    nome = None
    if request.method == 'POST':
        nome = request.form['nome']
    return render_template("login.html", nome= nome)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.route('/adduser',methods=['GET','POST'])
def adduser():
    messaggio= None
    if request.method =='POST':
        nome= request.form['nome']
        cognome= request.form['cognome']
        email = request.form['email']
        if nome:
            nuovo_utente = Utente(nome= nome, cognome = cognome, email= email)
            db.session.add(nuovo_utente)
            db.session.commit()
            messaggio = f'Utente {nome} aggiunto!'
    return render_template('adduser.html', messaggio = messaggio)

@app.route('/utenti')
def utenti():
    query = request.args.get('query','')
    if query :
        lista_utenti = Utente.query.filter(Utente.nome.ilike(f'%{query}%')).all()
    else:
        lista_utenti = Utente.query.all()
    return render_template('utenti.html', utenti = lista_utenti)

@app.route('/elimina/<int:id>')
def elimina(id):
    utente = Utente.query.get_or_404(id)
    db.session.delete(utente)
    db.session.commit()
    return redirect(url_for('utenti'))

@app.route('/modifica/<int:id>', methods=['GET','POST'])
def modifica(id):
    utente = Utente.query.get_or_404(id)
    if request.method == 'POST':
        nuovo_nome = request.form['nome']
        nuovo_cognome = request.form['cognome']
        nuova_email = request.form['email']
        utente.nome = nuovo_nome
        utente.cognome = nuovo_cognome
        utente.email = nuova_email
        db.session.commit()
        return redirect(url_for('utenti'))
    return render_template("modifica.html", utente =utente)
    

#Avvia l'app in modalità debug
if __name__=='__main__':
    app.run(debug=True)        #Con il debugger a true se c'è un errore ti da la possibilità di aprire una shell dope eseguire scripts di python 
                               #A codice finito va messo a false , è come lasciare una porta aperta al codice malevolo