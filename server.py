from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/my-link/')
def my_link():
    print('I got clicked!')

    return "You did it, you son of a cow!"


@app.route("/test", methods=["POST"])
def test():
    slider = request.form["slider"]
    return f"{slider} to zadany parametr"


@app.route("/login", methods=["POST"])
def login():
    user = request.form['nm']
    return f"{user} to Twoja nazwa użytkownika"


if __name__ == '__main__':
    app.run(debug=True)