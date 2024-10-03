from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def guess_home():
    return ("<h1> Guess a number between 0 and 9 </h1>"
            "<iframe src='https://giphy.com/embed/13RcbHeXlLNysE' width='480' height='302' style='' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>")


@app.route("/<int:guess>")
def guess_result(guess):
    if guess > random_number:
        return ("<h1> Your guess is too high! Guess again! </h1>"
                "<iframe src='https://giphy.com/embed/3og0IuWMpDm2PdTL8s' width='480' height='307' style='' frameBorder='0' class='giphy-embed' allowFullScreen></iframe><p><a href='https://giphy.com/gifs/redbull-3og0IuWMpDm2PdTL8s'></a></p>")
    elif guess < random_number:
        return ("<h1> Your guess is too low! Guess again! </h1>"
                "<iframe src='https://giphy.com/embed/IevhwxTcTgNlaaim73' width='480' height='269' style='' frameBorder='0' class='giphy-embed' allowFullScreen></iframe><p><a href='https://giphy.com/gifs/gsimedia-lowrider-gsi-chevytruck-IevhwxTcTgNlaaim73'></a></p>")
    else:
        return("<h1> You found me!</h1>"
               "<iframe src='https://giphy.com/embed/QyK8gRzGW2fV6qo8Hm' width='480' height='269' style='' frameBorder='0' class='giphy-embed' allowFullScreen></iframe><p><a href='https://giphy.com/gifs/wwe-monday-night-raw-bray-wyatt-firefly-fun-house-QyK8gRzGW2fV6qo8Hm'></a></p>")



if __name__ == "__main__":
    app.run(debug=True)
