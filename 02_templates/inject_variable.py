from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_name = "Mohammed Rizwan"
    name_list = my_name.split()
    info = {"Age":'34'}
    return render_template('inject_variable.html', name=my_name, name_list=name_list, info=info)

if __name__ == '__main__':
    app.run()
