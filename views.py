"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PythonWebProject import app
from PythonWebProject.RegistrationForm import RegistrationFrm
#import pandas as pd
#import os



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
   
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        colnames = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'class'],
        #here = os.path.dirname(os.path.abspath(__file__)),
        #here1= os.path.join(here, "iris.csv"),
        #dataset = read_csv("iris.csv",names=names),
        #df1 = pd.read_csv("iris.csv")      
        #dataset=pd.read_csv(app.open_resource("iris.csv"),names=['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'class'])
    )
   


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/register')
def register():
    form=RegistrationFrm()
    return render_template(
        'register.html',
         title='Register',
         message='Your application register page.',
         form=form
        )
