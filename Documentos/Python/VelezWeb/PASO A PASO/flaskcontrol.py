from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/users')
def user():
    # fake users
    users = [{'nick': 'Titi', 'name': 'Thiago'},
             {'nick': 'Fer', 'name': 'Fernanda'},
             {'nick': 'Leo', 'name': 'Leandro'},
    ]
    value = 12
    return render_template('users2.html',
                           users=users,
                           value=value)

if __name__ == "__main__":
    app.run(debug=True)
