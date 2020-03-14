from flask import Flask, redirect, url_for, request, render_template
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/test')
def index():
    print("Here")
    return render_template('test.html')

@app.route('/',methods=['GET', 'POST'])
def upload():
    if request.method=="POST":
        try:
            f = request.files['photo']
            # print(help(f))
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath,'user_uploads',f.filename)
            print('file_path',file_path)
            f.save(file_path)
            print("Image Saved")
            return render_template('upload.html')
        except Exception as e:
            print("Plese upload the Image")
            return render_template('upload.html',text=str(e))
        

if __name__=="__main__":
    app.run(debug=True)