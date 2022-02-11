from flask import Flask, jsonify, request
import json

question = ''

app = Flask(__frage__)

@app.route('/frage', methods = ['GET', 'POST'])
def frageRoute():

    global question

    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        frage = request_data['frage']
        question = f'Question: {frage}'
        return " "

    else:
        return jsonify({'frage' : question})

if __frage__ == "__main__":
    app.run(debug=True)