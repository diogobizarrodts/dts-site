
from flask import Flask, render_template, request, redirect, url_for, session
<<<<<<< HEAD
from flask import flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "segredo_dts"
app.permanent_session_lifetime = timedelta(minutes=30)

users = {
    "gerente": "1234",
    "funcionaria": "4321"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]
        if user in users and users[user] == pwd:
            session["user"] = user
            return redirect(url_for("painel"))
        else:
            flash("Credenciais inválidas. Tente novamente.")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/painel")
def painel():
    if "user" in session:
        return render_template("painel.html", user=session["user"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/enviar_contacto", methods=["POST"])
def enviar_contacto():
    nome = request.form["nome"]
    nif = request.form["nif"]
    telemovel = request.form["telemovel"]
    email = request.form["email"]
    servico = request.form["servico"]
    mensagem = request.form["mensagem"]
    print("Novo contacto:", nome, nif, telemovel, email, servico, mensagem)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
=======
import os

app = Flask(__name__)
app.secret_key = 'segredo_dts'

users = {
    'gerente': '1234',
    'funcionaria': '4321'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('contacto.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email in users and users[email] == senha:
            session['user'] = email
            return redirect(url_for('painel'))
        return "Credenciais inválidas"
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'user' in session:
        return render_template('painel.html', user=session['user'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
>>>>>>> a7634b581c68e6d49a511e199aaf12bd06cf68c5
