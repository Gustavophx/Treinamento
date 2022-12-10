from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app

# Criar um API flask
app = Flask(__name__)

# Criar uma instância de SQLAlchemy
# Use valores que sejam dificeis de desobrir
app.config['SECRET_KEY'] = 'FGS21515##$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# sqlite:/// e Local host, seguido do nome do bando de dados que desejamos mais .db

# Caso queira saber o Banco de dados pesquise no Google Connection string oracle/sql server ou nome do banco de dados

db = SQLAlchemy(app)
db: SQLAlchemy

# Definir a estrutura da tabela Postagem
# id_postagem, titulo, autor

class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    # comando .ForeignKey e utilizado pra fazer ligação entre 2 tabelas
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir a estrutura da rabela Autor
# id_autor, nome, email, senha, admin, postagens


class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')  # Utilizar o nome da "Class"

def inicializar_banco():
    # Executar o comando para criar o bando de dados
    with app.app_context():
        db.drop_all()
        db.create_all()

    # Criar usuários administradores
    autor = Autor(nome='gustavo', email='gustavo@email.com', senha='123', admin=True)
    with app.app_context():
        db.session.add(autor)
        db.session.commit()
if __name__ == "__main__":
    inicializar_banco()