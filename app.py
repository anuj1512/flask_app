"Flask api"
import flask
# from app import app
from flask import Flask, request, jsonify, render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',name="Anuj", place="Fatehpur")

@app.route('/about/<name>', methods=['GET'])
def aboutme(name):
    return f"Hi this is {name}"


@app.route('/uploadfile')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      print("file read")
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__=='__main__':
    app.run(debug=True)