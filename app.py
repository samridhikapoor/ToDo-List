from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def front():
    return render_template('index.html')

@app.route("/toodle-doit")
def display():
    return render_template('myg.html')
    
    # return render_template('display.html',app_data=app_data)

    
if __name__=="__main__":
    app.run(debug=True)