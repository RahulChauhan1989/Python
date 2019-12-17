"""
The flask application package.
"""
import uuid


from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = uuid.uuid4().hex  

import PythonWebProject.views
