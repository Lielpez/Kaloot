from flask import Flask, render_template
from os import listdir
from os.path import isfile, join
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    mypath=r'C:\Users\USER\Desktop\Kaloot\static\pictures'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    image_file=random.choice(onlyfiles)
    options=[image_file]
    onlyfiles.remove(image_file)
    options+=(random.sample(onlyfiles, 3))
    correct_answer=os.path.splitext(options[0])[0]
    for i in range (len(options)):
        options[i]=os.path.splitext(options[i])[0]
    random.shuffle(options)
    return render_template('game.html',options=options,image_file=image_file,correct_answer=correct_answer)

if __name__ == '__main__':
    app.run(debug=True)