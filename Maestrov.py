#!/usr/bin/env python3

import markovify
import pysynth
import shutil
import os

from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

def generateSong():

    noteList=[]

    with open("./notes.txt") as f:
        text = f.read()

    text_model = markovify.NewlineText(text)

    for i in range(7):
        z =(text_model.make_short_sentence(100))
        if (z != None and len(z) > 16):
            x = z

    count = 0
    listCount = 0

    for i in x:
        if (i != " " and i != "#"):         
            noteList.insert(listCount,i)
            listCount +=1
        count +=1

    if(os.path.isfile('./static/tune.wav')):
        print("Deleting old WAV file")
        os.remove("./static/tune.wav")

    tune = ((noteList[0], 4), (noteList[1], 4), (noteList[2], 4), (noteList[3], 4), (noteList[4], 4), (noteList[5], 4), (noteList[6], 4), (noteList[7], 4))
    print("Creating new WAV file")
    pysynth.make_wav(tune, fn = "./static/tune.wav")
    
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/GenerateSong')
def result():
    generateSong()
    return '''
        <audio controls id='audio'>
        </audio>
        '''
        
if __name__ == "__main__":
    app.run()