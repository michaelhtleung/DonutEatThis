import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)


@app.route('/uploadImage')
def render_index():
    return render_template("index.html")


@app.route('/', methods=['GET','POST'])
def upload_img():
    print ('upload image called')
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        print ('in POST')
        img = request.files['file']
        print ('received image')
        # img.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename)))
        print ('saved image')
        return 'image uploaded!'
    return 'image not uploaded...'