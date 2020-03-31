from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home ():

    return "<h1>Hello Aman</h1>"


@app.route('/blog', methods=['GET','POST'])
def blog ():

    return "Welcome to my first blog page."

if __name__ == "__main__":
    app.run(debug=True)