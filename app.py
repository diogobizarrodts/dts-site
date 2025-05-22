from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_dts'

# Utilizadores
users = {
    "gerente@dts.pt": "1234",
    "funcionaria@dts.pt": "4321"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/enviar_contacto', methods=['POST'])
def enviar_contacto():
    dados = request.form.to_dict()
    print("Novo contacto recebido:", dados)
    return "Obrigado pelo seu contacto!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email in users and users[email] == senha:
            session['user'] = email
            return redirect(url_for('painel'))
        return render_template('login.html', erro='Credenciais inválidas.')
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('painel.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
