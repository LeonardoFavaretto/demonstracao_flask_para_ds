import joblib
import pandas as pd

from flask import Flask, request, jsonify

MODEL = joblib.load('model')

app = Flask(__name__)
@app.route('/')

def fire_app():
    choveu = request.args.get("choveu")
    temperatura = request.args.get("temp")
    
    try:
        choveu = bool(choveu) 

    except ValueError:
        return ('It only accepts 1 or 0.')

    try:
        temperatura = float(temperatura)
    except ValueError:
        return ('It only accepts numeric values.')
    
    return run_model(choveu, temperatura)

def run_model(choveu, temperatura):

    data = pd.DataFrame({
    'temperatura_hoje': [temperatura],
    'choveu': [choveu]
        })

    output = MODEL.predict(data)


    return jsonify({'temperatura_amanha': str(output[0])})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
