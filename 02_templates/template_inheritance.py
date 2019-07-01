from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ihome.html')

@app.route('/user/<name>')
def main(name):
    return render_template('imain.html', user=name)

if __name__ == '__main__':
    app.run()
