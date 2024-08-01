from flask import Flask, render_template
from flask_wtf import FlaskForm # type: ignore
from wt_form import FileField, SubmitField # type: ignore



class UploadFileForm(FlaskForm):
    file = FileField("File")
    subit = SubmitField("Upload File")

@app.route(/fileupload, methods = 'GET', "POST") # type: ignore
def fileupload():
    form = UploadFileForm()
    return(render_template('fileupload.html', form = form))

