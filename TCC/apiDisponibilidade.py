import flask
from flask import request, jsonify
import joblib
import json
import numpy as np

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class Disponibilidade:
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo
        self.loaded_model = joblib.load(self.nomeArquivo)

    def execute(self, disp):
        disp = np.asarray([disp])
        response = self.loaded_model.predict(disp)
        probs = self.loaded_model.predict_proba(disp)
        probs = probs.round(2)
        print(probs[:, 0])
        data_set = {"chance_Ativa": str(probs[:, 0]), "chance_Inativa": str(probs[:, 1])}
        response = json.dumps(data_set)
        print(response)
        return response

obj = Disponibilidade('random_forest_disp.sav')

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/disponibilidade/verifica', methods=['POST'])
def api_disponibilidade():
    if request.method == "POST":
        main_list = []
        IPs2 = request.json
        for i in IPs2:
            main_list.append(i)
        r = obj.execute(main_list)

        return r
    else:
	    return jsonify("Only exists POST")
    

app.run()


