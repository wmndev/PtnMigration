from flask import Flask, render_template, request, json
import cx_Oracle


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/showToolForm')
def showToolForm():
    return render_template("toolForm.html")

@app.route('/startTool', methods=['POST'])
def startTool():
    _query = request.form['selectQuery']
    print _query

if __name__ == '__main__':
    app.run()
