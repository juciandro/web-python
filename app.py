#print("Hello world")
#importa a biblioteca
from flask import Flask
#cria o app
app = Flask("meu app")
#cria uma rota
@app.route('/')
def main():
    return 'Hello World'

@app.route('/newpage')
def newpage():
    return '<h1>Primeiro codigo em Python usando o Framework Flask</h1>'