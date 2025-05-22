from flask import Flask, render_template, request, redirect, url_for, session

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
    app.run(debug=True)
