from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('findex.html')

@app.route('/signup')
def signup():
    return render_template('fsignup.html')

@app.route('/thankyou')
def thankyou():
    first_name = request.args.get('firstname')
    last_name = request.args.get('lastname')

    return render_template('fthankyou.html',first_name=first_name, last_name=last_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('f404.html'), 404

if __name__ == '__main__':
    app.run()
