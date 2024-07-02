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
app = flask.Flask(__name__)


 
@app.route("/")
def home():
    a_img = list(choice(arrow_img))#choice(arrow_img) list yok çünkü os.listdir list döner
    return a_img#f"<img src='images/arrow images/{a_img}'>" burda direkt olarak a_img dersen sana string döner image(resim) dönmez


if __name__ == "__main__":
    app.run(debug=True)