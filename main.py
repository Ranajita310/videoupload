# Import Libraries below
import os
import cv2
from flask import  Flask, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route("/")

# Define flask 
#def flask():


@app.route('/',methods=['POST'])
# Define upload_form() and route the webapp 
def upload_form():
     return render_template("upload.html")

# Define upload_video() to get video in defined folder and route the webapp  
def upload_video():
    file=request.files["file"]
    filename=secure_filename(file.filename)
    file.save(os.path.join('static/',filename))
    return render_template("upload.html",filename=secure)
    @app.route('/display/')



# Define display_video() to Display video in defined folder and route the webapp  
    def display_video(filename):
        return redirect("upload.html",url_for('static',filename=filename))




if __name__ == "__main__":
    app.run(debug=True)
