from flask import Flask, render_template, request, redirect, flash, url_for,session
import requests, json

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_palabra', methods=['POST','GET'])
def buscar_palabra():
    session['palabra'] = request.form['palabra']
    idioma = request.form['idioma']
    #guna = request.form['guna']
    print(idioma)
    json_data = requests.request("GET", "http://127.0.0.1:8000/diccionarioguna/api/v1.0/palabras")
    json_dataguna = requests.request("GET", "http://127.0.0.1:8000/diccionarioguna/api/v1.0/espanol")
    data = json.loads(json_data.text)
    dataguna = json.loads(json_dataguna.text)
    x=0
    sinonimos=[]
    definicones=[]
    if idioma == 'guna':
        if session['palabra'] == "":
            flash('Inserte una palabra')
        else:
            for x in range(len(data)):
                if data[x]['palabra'] == session['palabra']:
                    if len(data[x]['sinonimos']) > 0:
                        y=0
                        for y in range(len(data[x]['sinonimos'])):
                            sinonimos = data[x]['sinonimos']
                    y=0
                    for y in range(len(data[x]['definicion'])):
                        definicones = data[x]['definicion']
                x+=1
        if len(sinonimos) == 0 and len(definicones)==0 and session['palabra'] != "":
            flash('Palabra no encontrada')
        respuesta=render_template("index.html", s=sinonimos, d=definicones,p=session['palabra'])
    elif idioma=='espanol':
        if session['palabra'] == "":
            flash('Inserte una palabra')
        else:
            for x in range(len(dataguna)):
                if session['palabra'] in dataguna[x]['palabra']:
                        y=0
                        for y in range(len(dataguna[x]['definicion'])):
                            definicones = dataguna[x]['definicion']
                x+=1
        if len(definicones)==0 and session['palabra'] != "":
            flash('Palabra no encontrada')
        respuesta=render_template("index.html", d=definicones,p=session['palabra'])
    return respuesta



if __name__ == "__main__":
    app.run()
