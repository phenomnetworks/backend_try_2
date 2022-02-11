from flask import Flask, jsonify, request
import json

response = ''
response2 = ''

app = Flask(__name__)

@app.route('/name', methods = ['GET', 'POST'])
def nameRoute():

    global response
    global response2

    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        name = request_data['name']
        response = f'Hallo {name}! Das ist Python'
        response2 = f'Dein Name ist also {name}, richtig?'
        return " "

    else:
        return jsonify({'name' : response}, {'name' : response2})        

if __name__ == "__main__":
    app.run(debug=True)
