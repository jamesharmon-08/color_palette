from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'


@app.route('/')
def home():
    file="me3.jpg"
    return render_template("index.html", file=file)


@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        img_file = request.files['file']
        if img_file.filename != "":
            img_file.save('static/'+ img_file.filename)
    img=Image.open(img_file).convert(mode="HSV")

    color_array = np.array(img)
    h_arr = color_array[:,0]
    s_arr = color_array[:,1].copy()
    v_arr = color_array[:,2].copy()
    print(f'The size of the array is {color_array.shape}')

    saturation = s_arr.mean()
    value=v_arr.mean()
    (unique, counts) = np.unique(h_arr, return_counts=True)
    frequency = np.asarray((unique, counts)).T
    print(frequency*359//255)
    print(saturation)
    print(value)
    return render_template('index.html',file=img_file.filename)

if __name__ == "__main__":
    app.run(debug=True)
