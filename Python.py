from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__,template_folder='')

freezer=Freezer(app)
if __name__== '__main__':
    freezer.freeze()



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    value = request.form['test']
    return value

if __name__ == '__main__':
    app.run()
