import data_pipeline as dp

import io
import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)


def render_index():
    return render_template("index.html")


# @app.route('/uploadImage')
@app.route('/', methods=['GET','POST'])
def upload_img():
    print ('upload image called')
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        print ('in POST')
        img = request.files['file']
        print ('received image')

        path = os.path.abspath('test_img.jpeg')
        img.save(path)
        print('wrote image')
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        print('read image')

        payload = dp.process_image(path=path, content=content)
        print('image processed!')
        return jsonify(payload=payload)

    return '!!! !!! !!! image not uploaded...'
