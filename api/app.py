from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def home():
    title = "Home"
    return render_template("home.htm", title=title)


@app.route('/academico')
def academico():
    projetos = [{"nome": "Portfólio Digital", "img": "../static/img/img-portfolio-digital500.png", "link": "https://github.com/eberssj/portfolio_digital_dsm"}, 
    {"nome": "Desafio - DevWeb I", "img": "../static/img/speaknow500.png", "link": "https://github.com/eberssj/desafio-speaknow"}, 
    {"nome": "API II - Nefrologia", "img": "../static/img/img-api500.png", "link": "https://github.com/TeamHiveAPI/API-2023.2"}]
    title = "Acadêmico"
    return render_template("academico.htm", title=title, projetos=projetos)


@app.route('/sobre')
def sobre():
    title = "Sobre mim"
    return render_template("sobre.htm", title=title)


if __name__ == '__main__':
    app.run(debug=True)