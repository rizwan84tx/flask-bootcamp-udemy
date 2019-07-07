from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "<h2>Welcome to Puppy Latin Exercise!!</h2>"

@app.route('/puppy_latin/<name>')
def puppy(name):
    if name[-1].upper() == 'Y':
        puppy_latin = name[:-1]+'iful'
    else:
        puppy_latin = name+'y'

    return "<h2>Hi {} <br>Your Puppy Latin name: {}</h2>".format(name, puppy_latin)

if __name__ == '__main__':
    app.run()
