from flask import Flask, request, jsonify, json
app = Flask(__name__)

json_data=open("../Pruebas/palabras.json").read()
json_dataguna=open("../Pruebas/guna.json").read()
data = json.loads(json_data)
dataguna = json.loads(json_dataguna)

@app.route('/diccionarioguna/api/v1.0/palabras', methods=['GET','POST'])
def get_tareas():
    if request.method == "GET":
        print(request.environ)
        return jsonify(data)

@app.route('/diccionarioguna/api/v1.0/espanol', methods=['GET','POST'])
def get_guna():
    if request.method == "GET":
        print(request.environ)
        return jsonify(dataguna)

if __name__ == "__main__":
    app.run(port="8000")
