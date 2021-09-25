from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index() :
    if request.method == 'GET':
        return render_template('index.html', title='')
    if request.method == 'POST':
        url = 'https://selectflowers.herokuapp.com'
        data = [[float(request.form['list1']),
                 float(request.form['list2']),
                 float(request.form['list3']),
                 float(request.form['list4'])]]
        print(data)
        response = requests.post(url, json=data)
        print(response.text)


        return render_template('index.html', title="Это: " + response.text)


if __name__ == '__main__' :
    app.run(port=5000, host='127.0.0.1')
