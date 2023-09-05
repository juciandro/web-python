#print("Hello world")
#importa a biblioteca
from flask import Flask, render_template
from flask import render_template
#cria o app
app = Flask("meu app")
#cria uma rota
#@app.route('/')
#def main():
#    return 'Hello World'

#@app.route('/newpage')
#def newpage():
#    return '<h1>Primeiro codigo em Python usando o Framework Flask.</h1>'

posts = [
    {
        "titulo":"Minha primeira postagem",
        "texto":"Esse é um texto"
    },
    {
        "titulo":"Segundo post",
        "texto":"Outro teste"
    }

]   

@app.route('/')
def exibir_entradas():
    entradas = posts
    return render_template("exibir_entradas.html", entradas=entradas)