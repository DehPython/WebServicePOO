from app import app
from flask import render_template, request
from app.models.forms import LoginForm

posts = [
    {
        'author': 'Andre Martins',
        'title': 'POO é a melhor matéria de todas',
        'content': 'O professor vinicius ensina muito bem e nos ajudar a entender a aula!',
        'date_posted': '09 de fevereiro de 2023'
    },
    {
        'author': 'João Souza',
        'title': 'Como é legal estudar na UFG',
        'content': 'Hoje tive a certeza que foi a melhor escolha a minha vida',
        'date_posted': '09 de fevereiro de 2023'
    }
]

app.secret_key = 'andre340'

#Home Page / Login
@app.route("/", methods=['GET'])
def index():
    return render_template('login.html')

@app.route("/logar", methods=['POST'])
def logar():
    usr = request.form['usuario']
    pswrd = request.form['senha']
    if usr == 'andre':
        return render_template('home.html', posts=posts)
    else:
        return render_template('login.html', msg='Usuario Inexistente !! Digite novamente')

#Pagina email recuperação
@app.route("/esqueci", methods=['GET'])
def esqueci():
        return render_template('esqueci.html')

#Pagina Sucesso recuperação
@app.route("/recuperacao", methods=['GET'])
def recuperacao():
        return render_template('recuperacao.html', msg='Formulario de recuperação de senha enviado com SUCESSO !')

#Pagina de cadastro
@app.route("/cadastro", methods=['GET'])
def cadastro():
    return render_template('cadastro.html')

#Pagina de cadastro sucesso
@app.route("/cadastrado", methods=['GET'])
def cadastrado():
    return render_template('cadastrado.html', msg='Cadastro feito com SUCESSO !')

#Pagina de home do usuario
@app.route("/home")
def homepage():
    return render_template('home.html', posts=posts)

#Pagina de criação de conteudo
@app.route("/criar")
def criar():
    return render_template('criar.html')

@app.route("/notify")
def notify():
    return render_template('notify.html')

@app.route("/configuracoes")
def configuracoes():
    return render_template('configuracoes.html')

@app.route("/politica-privacidade")
def privacidade():
    return render_template('politica-privacidade.html')

@app.route("/perfil")
def perfil():
    return render_template('perfil.html')