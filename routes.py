import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)


@app.route('/')
def hello():
    return 'goodbye, World!'

@app.route('/uploadImage', methods=['GET','POST'])
def upload_img():
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        img = request.files['product_img']
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename)))
        return 'image uploaded!'
    return 'image not uploaded...'