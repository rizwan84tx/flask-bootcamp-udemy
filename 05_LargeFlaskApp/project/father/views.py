# views.py - father
from flask import Blueprint,render_template,redirect,url_for
from project import db
from project.models import Father
from project.father.forms import AddForm

father_blueprint = Blueprint('father', __name__, template_folder='templates/father')

@father_blueprint.route('/add', methods=['GET','POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        child_id = form.child_id.data
        new_father = Father(name,child_id)
        db.session.add(new_father)
        db.session.commit()
        return redirect(url_for('child.list'))

    return render_template('add_father.html', form=form)
