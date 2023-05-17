from flask import Flask
from pathlib import Path
import numpy
app = Flask(__name__)
 
@app.route('/')
def hello():
   
    my_file = Path("cancer_data/cancer.csv")
    if my_file.is_file():
        f = open("cancer_data/cancer.csv", "r")
        return f.readline()
    else:
        return "File has not been added by DVC"
 
if __name__ == '__main__':
   app.run()