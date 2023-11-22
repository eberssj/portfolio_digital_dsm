from flask import Flask, render_template
from jinja2 import Template

app = Flask("__name__")


@app.route('/')
def home():
    title = "Home"
    return render_template("home.htm", title=title)


@app.route('/academico')
def academico():
    title = "Acadêmico"
    return render_template("academico.htm", title=title)


@app.route('/sobre')
def sobre():
    title = "Sobre mim"
    return render_template("sobre.htm", title=title)


if __name__ == '__main__':
    app.run(host='10.8.0.1')