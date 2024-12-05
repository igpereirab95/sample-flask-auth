from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd123' # chave de seguranca, senha do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # local onde esta o arquivo do sqlite

db = SQLAlchemy(app)



@app.route("/hello-world", methods=["GET"])
def hello_wolrd():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)