import data_pipeline as dp

import io
import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/scan_all')
def render_scan_all():
    return render_template("scan-all.html")

# @app.route('/scan_safe')
# def render_scan_safe():
#     return render_template("scan-safe.html")

# @app.route('/scan_unsafe')
# def render_scan_unsafe():
#     return render_template("scan-unsafe.html")

@app.route('/ingredients')
def render_ingredients():
    return render_template("ingredient.html")

@app.route('/uploadImage', methods=['GET','POST'])
def upload_img():
    print ('upload image called')
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        pass
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

    # print ('ok whatever redirect then')
    # return redirect(url_for('render_scan_all'))
