from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/my-link')
def my_link():
    print('I got clicked!')
    return "You did it, you son of a cow!"


@app.route('/test', methods=["POST"])
def test():
    slider = request.form["slider"]
    return f"{slider} to zadany parametr"


@app.route('/login', methods=["POST"])
def login():
    user = request.form['nm']
    return f"{user} to Twoja nazwa użytkownika"


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form.html' to submit form.html"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form=form_data)



if __name__ == '__main__':
    app.run(debug=True)
