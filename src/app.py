from flask import Flask, flash, request, redirect, url_for, render_template, send_file
import urllib.request
import os
from werkzeug.utils import secure_filename
import image_compressor as ic
from datetime import datetime
# from dotenv import load_dotenv
# dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
# load_dotenv(dotenv_path)
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "tubes2algeo"
app.config['ENV'] = 'development'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB max sizes
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('Gambar gagal diupload')
        return redirect(request.url)
    file = request.files['file']            # get image file
    if file.filename == '':
        flash('Tidak ada gambar yang dipilih')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        k = 100 - int(request.form['compressRate'])
        print(k)
        start_time = datetime.now()	
        ic.img_comp(f'{UPLOAD_FOLDER}{file.filename}',k)
        end_time = datetime.now()
        duration = end_time - start_time

        savename,ext = os.path.splitext(filename)
        savename = f'{UPLOAD_FOLDER}{savename}Compressed{ext}'
        uploadFilename = f'{UPLOAD_FOLDER}{filename}'
        size_before = os.path.getsize(uploadFilename)
        size_after = os.path.getsize(savename)
        compression_rate = (size_after / size_before) * 100

        return render_template('index.html', filename=filename, duration = duration, compression_rate = compression_rate)
    else:
        flash('Gambar harus memiliki ekstensi png, jpg, atau jpeg')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename ), code=301)

@app.route('/display/<filename>/c')
def display_image_c(filename):
    savename,ext = os.path.splitext(filename)
    savename = f'{savename}Compressed{ext}'
    return redirect(url_for('static', filename='uploads/' + savename, ), code=301)
 
@app.route('/download/<filename>')
def download_file(filename):
    savename,ext = os.path.splitext(filename)
    savename = f'{UPLOAD_FOLDER}{savename}Compressed{ext}'
    return send_file(savename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)