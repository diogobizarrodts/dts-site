<<<<<<< HEAD

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'segredo_dts'

users = {
    'gerente': '1234',
    'funcionaria': '4321'
=======
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_dts'

# Utilizadores
users = {
    "gerente@dts.pt": "1234",
    "funcionaria@dts.pt": "4321"
>>>>>>> 1d7ded26f66b120f954ecbe53e8c51029c665eb5
}

@app.route('/')
def home():
<<<<<<< HEAD
    return render_template('index.html')
=======
    return render_template('home.html')
>>>>>>> 1d7ded26f66b120f954ecbe53e8c51029c665eb5

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

<<<<<<< HEAD
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Aqui podes processar o formulário se quiseres
        return redirect(url_for('home'))
    return render_template('contacto.html')

=======
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/enviar_contacto', methods=['POST'])
def enviar_contacto():
    dados = request.form.to_dict()
    print("Novo contacto recebido:", dados)
    return "Obrigado pelo seu contacto!"

>>>>>>> 1d7ded26f66b120f954ecbe53e8c51029c665eb5
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email in users and users[email] == senha:
            session['user'] = email
            return redirect(url_for('painel'))
<<<<<<< HEAD
        return "Credenciais inválidas"
=======
        return render_template('login.html', erro='Credenciais inválidas.')
>>>>>>> 1d7ded26f66b120f954ecbe53e8c51029c665eb5
    return render_template('login.html')

@app.route('/painel')
def painel():
<<<<<<< HEAD
    if 'user' in session:
        return render_template('painel.html', user=session['user'])
    return redirect(url_for('login'))
=======
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('painel.html', user=session['user'])
>>>>>>> 1d7ded26f66b120f954ecbe53e8c51029c665eb5

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
