#!/usr/bin/python3
"""
starts a Flask web application
"""
import sys

sys.path.insert(1, '/home/iyanu/Documents/Wordle/engine')

from flask import Flask, render_template, url_for, request, redirect
from main import Game
from wordhelper.wordchecker import real
import json

app = Flask(__name__)

history = []
round = Game()
round.start()
print(round.answer)

@app.route('/', strict_slashes=False, methods=['POST', 'GET'])
def index():
    """Under condstruction"""
    in_word = ""
    input_list = []
    won = ""
    if request.method == 'POST':
        for char in request.form.values():
            if char == "Check":
                pass
            else:
                input_list.append(char)
                in_word += char
        if round.gamerun(in_word) == False:
            round.tries -= 1
            history.append(in_word)
        else:
            won = "Winner"
        return redirect('/')
    else:
        return render_template("wordle.html", histories=history, tries=round.tries, msg=won)


@app.route('/delete_last', strict_slashes=False)
def deleteLastHis():
    if len(history) <= 0:
        return index()
    history.pop()
    return index()

@app.route('/delete', strict_slashes=False)
def deleteHis():
    if len(history) <= 0:
        return index()
    while len(history) > 0:
        history.pop()
    return index()

@app.route('/check', strict_slashes=False, methods=["POST", "GET"])
def check():
    
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
