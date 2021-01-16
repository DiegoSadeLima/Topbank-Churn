

from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

colunas = ["CreditScore","Geography","Gender","Age","Tenure","Balance",
           "NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary"]


modelo = pickle.load(open('modelo.sav','rb'))

app = Flask(__name__)


@app.route('/Topbank/', methods=['POST'])


def Topbank():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    churn = modelo.predict([dados_input])
    return jsonify(churn)

app.run(debug=True, host="0.0.0.0")