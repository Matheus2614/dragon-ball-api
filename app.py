from flask import Flask, request, render_template, redirect
import requests, random

app = Flask(__name__)


API = 'https://dragonball-api.com/api/characters/'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    idade = int(request.form.get('idade'))

    if idade > 100 or idade < 0:
        return render_template('index.html', erro="Você deve colocar uma idade válida!")
    
    else:
        idade = 0

        numero_aleatorio = random.randint(0,57)
        personagem = idade + numero_aleatorio
        print(personagem)
        response = requests.get(API + str(personagem))

    if response.status_code == 200:
        data = response.json()
        img = data['image']
        nome = data['name']
        race = data['race']
        ki = data['ki']
        return render_template('index.html',personagem=personagem, nome=nome, race=race,ki=ki, img=img)
    else:
        return render_template('index.html', erro="Erro no sistema! Volte outra hora.")

if __name__ == '__main__':
    app.run()
