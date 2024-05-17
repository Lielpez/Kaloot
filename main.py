from flask import Flask, render_template, request, redirect, url_for
from os import listdir, makedirs
from os.path import isfile, join, splitext, exists
import os
import random
import shutil
from PIL import Image
from pillow_heif import register_heif_opener

app = Flask(__name__)
UPLOAD_FOLDER = 'static/pictures'

# Ensure the upload folder exists
if not exists(UPLOAD_FOLDER):
    makedirs(UPLOAD_FOLDER)

# Register HEIF opener
register_heif_opener()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'files' not in request.files:
            return 'No file part'
        
        files = request.files.getlist('files')
        
        # Clear the upload folder before saving new files
        shutil.rmtree(UPLOAD_FOLDER)
        makedirs(UPLOAD_FOLDER)

        for file in files:
            if file and file.filename != '':
                file_name = os.path.basename(file.filename)
                file_path = join(UPLOAD_FOLDER, file_name)
                file.save(file_path)

                # Check if the file is a HEIC file and convert it to JPEG
                if file_name.lower().endswith('.heic'):
                    heic_to_jpeg(file_path)
        return redirect(url_for('game'))
    
    return render_template('upload.html')

def heic_to_jpeg(heic_path):
    # Open the HEIC file using Pillow with pillow-heif
    image = Image.open(heic_path)
    
    # Create the JPEG file path
    jpeg_path = splitext(heic_path)[0] + '.jpg'
    
    # Save the image as JPEG
    image.save(jpeg_path, 'JPEG')
    
    # Remove the original HEIC file
    os.remove(heic_path)

@app.route('/game')
def game():
    mypath = UPLOAD_FOLDER
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    if not onlyfiles:
        return 'No images found in the uploaded folder. Please upload images first.'
    
    image_file = random.choice(onlyfiles)
    options = [image_file]
    onlyfiles.remove(image_file)
    options += (random.sample(onlyfiles, 3))
    correct_answer = splitext(options[0])[0]
    
    for i in range(len(options)):
        options[i] = splitext(options[i])[0]
    
    random.shuffle(options)
    
    return render_template('game.html', options=options, image_file=image_file, correct_answer=correct_answer)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')