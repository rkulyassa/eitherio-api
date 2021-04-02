import flask
from flask import request, jsonify
from eitherapi import Eitherio

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/question', methods=['GET'])
def question():
        return jsonify(Eitherio().get_question())

app.run()
