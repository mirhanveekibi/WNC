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
from flask import request,jsonify
 
#* variables
arrow_img = listdir("static/img/arrow_images")
question_img = listdir("static/img/animals")
visiter_ip = ""
a_img = ""
q_img = ""
vpm = {}
 
#* flask app setup
app = flask.Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    global a_img, q_img, visiter_ip
    a_img = choice(arrow_img)
    q_img = choice(question_img)
    visiter_ip = request.remote_addr
    return flask.render_template("index.html",img1=f"static/img/arrow_images/{a_img}",img2=f"/static/img/animals/{q_img}")

if __name__ == "__main__":
    app.run(debug=True)