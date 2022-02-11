from flask import Flask, jsonify, request, request2
import json

response = ''
response2 = ''

app = Flask(__name__)

@app.route('/name', methods = ['GET', 'POST'])
def nameRoute():

    global response

    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        name = request_data['name']
        response = f'Hallo {name}! Das ist Python'
        return " "

    else:
        return jsonify({'name' : response})   

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/name2', methods = ['GET', 'POST'])
def nameRoute2():

    global response2

    if(request.method == 'POST'):
        request_data2 = request.data
        request_data2 = json.loads(request_data2.decode('utf-8'))
        name2 = request_data2['name2']
        response2 = f'Dein Name ist also {name2}, richtig?'
        return " "

    else:
        return jsonify({'name2' : response2})   

if __name__ == "__main__":
    app.run(debug=True)
