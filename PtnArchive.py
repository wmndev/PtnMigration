from flask import Flask, render_template, request

from resources import connections

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/showToolForm')
def showToolForm():

    # ---------Tool initial Settings ------
    connections.loadSettings()
    # -------------------------------------

    return render_template("toolForm.html", owners=getAllOwners())


@app.route('/startTool', methods=['POST'])
def startTool():
    _query = request.form['selectQuery']


def getAllOwners():
    return ["HR4_PROD", "HR5_UAT", "TRM_JPMC"]  # get all owners list


if __name__ == '__main__':
    app.run()
