#

#* ░██╗░░░░░░░██╗███╗░░██╗░█████╗░
#* ░██║░░██╗░░██║████╗░██║██╔══██╗
#* ░╚██╗████╗██╔╝██╔██╗██║██║░░╚═╝
#* ░░████╔═████║░██║╚████║██║░░██╗
#* ░░╚██╔╝░╚██╔╝░██║░╚███║╚█████╔╝
#* ░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝░╚════╝░

#* libraries
from os import listdir
from shutil import copyfile
from random import randint,choice
import flask

#* variables
arrow_img = listdir("images/arrow images")
question_img = listdir("images/db")



#* flask app setup
app = flask.Flask(__name__)


 
@app.route("/")
def home():
    a_img = choice(arrow_img)
    return f"<img src='images/arrow images/{a_img}' alt='404 Not Found'>"

if __name__ == "__main__":
    app.run(debug=True)