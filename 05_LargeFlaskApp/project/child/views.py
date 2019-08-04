# views.py - child
from flask import Blueprint,render_template,redirect,url_for
from project import db
from project.models import Child
from project.child.forms import AddForm, DelForm

child_blueprint = Blueprint('child', __name__, template_folder='templates/child')

@child_blueprint.route('/add', methods=['GET','POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_child = Child(name)
        db.session.add(new_child)
        db.session.commit()
        return redirect(url_for('child.list'))

    return render_template('add_child.html', form=form)


@child_blueprint.route('/list')
def list():
    children = Child.query.all()
    return render_template('list_child.html', children=children)


@child_blueprint.route('/delete', methods=['GET','POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        cid = form.id.data
        remove_child = Child.query.get(cid)
        db.session.delete(remove_child)
        db.session.commit()
        return redirect(url_for('child.list'))

    return render_template('delete_child.html', form=form)
