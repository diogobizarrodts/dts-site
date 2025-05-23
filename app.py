
from flask import Flask, render_template, request, redirect, url_for, session
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
