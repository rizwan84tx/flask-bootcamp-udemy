from flask import Flask

app = Flask(__name__)

@app.route('/family/')
def main():
    return "<h1>Family Page!!</h1>"

@app.route('/family/<name>')
def family(name):
    return "<h1>{} family welcomes you!!</h1>".format(name.upper())

if __name__ == '__main__':
    app.run()
