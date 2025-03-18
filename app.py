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
        erro = "Você deve colocar uma idade válida!"
        return render_template('index.html', erro=erro)
    
    else:
        idade = 0

        numero_aleatorio = random.randint(1,44)
        personagem = idade + numero_aleatorio
        print(personagem)

        if personagem == 36 or personagem == 41:
            personagem = idade + numero_aleatorio
            response = request.get(API + str(personagem))

        else:
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
