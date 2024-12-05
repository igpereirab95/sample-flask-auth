from app import db

class User(db.Model):
    # id (int), username (text), password (text)
    id = db.Column(db.Integer, primary_key=True) # definicoes do que a coluna armazenara. Setando chave primaria
    username = db.Column(db.String(80), nullable=False, unique=True) # setar valor vazio ou nao e tamanho do nome de usuario
    password = db.Column(db.String(80), nullable=False)