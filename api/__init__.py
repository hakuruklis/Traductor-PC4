from flask import Flask, request, jsonify
import json, pprint
app = Flask(__name__)

json_data=open("../Pruebas/palabras.json").read()
data = json.loads(json_data)

@app.route('/diccionarioguna/api/v1.0/palabras', methods=['GET'])
def get_tareas():
    if request.method == "GET":
        print(request.environ)
        return jsonify(data)

if __name__ == "__main__":
    app.run()