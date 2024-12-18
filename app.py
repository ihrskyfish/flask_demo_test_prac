from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/template')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    print("dddddd")
    # app.run()
    app.run(debug=True)
    print("dddddd")
