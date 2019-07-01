from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = ['T-REX', 'ANKYLO', 'STEGGO', 'IGUANO']
    return render_template('control_flow.html', user=user)

if __name__ == '__main__':
    app.run()
