from flask import Flask, url_for, render_template

# inicialização
app = Flask(__name__)

#rotas
@app.route("/")
def home():
    titulo = "Gestão de Usuários"
    usuários = [
        {"name": "Jânderson", "user_active": True},
        {"name": "Jonas", "user_active": False},
        {"name": "Maria", "user_active": True},
        {"name": "Socorro", "user_active": False}
    ]
    return render_template('index.html', title = titulo, users = usuários)


@app.route("/about")
def pag_about():
    return f"""
        <h1>Meu nome é Jânderson</h1>
        <p>eu sou programador Python</p>
        <a href='{url_for('home')}'>retornar ao home</a>
    """


# execução
app.run(debug = True)