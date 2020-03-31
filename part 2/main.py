from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home ():

    return render_template('home.htm', title="homepage" , username='Aman Singh')



@app.route('/blog', methods=['GET','POST'])
def blog ():

    posts = [
        {
            'username' : 'Aman Singh',
            'date' : '12/03/20',
            'content' : 'Today is sunday'
        },
        {
            'username' : 'Raghav',
            'date' : '14/03/20',
            'content' : 'Today is Monday, enjoying coffee.'
        },
        {
            'username' : 'Sam',
            'date' : '15/03/20',
            'content' : 'Today is tuesday, Fitness is important.'
        },
        {
            'username' : 'Smriti',
            'date' : '16/03/20',
            'content' : 'Today is wedneday, Having Breakfast'
        }
    ]

    return render_template('blog.htm', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)