from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/user_template')
def user():
    username = {'nick': 'Leo',
                'name': 'Rami la golosa'}  # fake user
    return render_template('user.html',
                           user=username,
                           muestra=app.name)

if __name__ == "__main__":
    app.run(debug=True)
