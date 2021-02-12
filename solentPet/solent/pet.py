from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from solent.auth import login_required
from solent.db import get_db

bp = Blueprint('pet', __name__)


@bp.route('/')
def index():
    db = get_db()
    pets = db.execute(
       'SELECT p.id, name, type, breed, description, hobbies'
        ' FROM pet p'
        ' ORDER BY name'
    ).fetchall()
    return render_template('pet/index.html',pets = pets)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        breed = request.form['breed']
        description = request.form['description']
        hobbies = request.form['hobbies']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO pet (name, type, breed, description, hobbies)'
                ' VALUES (?, ?, ?, ?, ?)',
                (name, type,breed,description,hobbies)
            )
            db.commit()
            return redirect(url_for('pet.index'))

    return render_template('pet/create.html')

def get_pet(id, check_author=True):
    pet = get_db().execute(
        'SELECT p.id, name, type, breed, description, hobbies'
        ' FROM pet p '
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if pet is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    return pet

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    pet = get_pet(id)

    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        breed = request.form['breed']
        description = request.form['description']
        hobbies = request.form['hobbies']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET name = ?, type = ?, breed = ?, description = ?, hobbies = ?'
                ' WHERE id = ?',
                (name, type, breed, description, hobbies, id)
            )
            db.commit()
            return redirect(url_for('pet.index'))

    return render_template('pet/update.html', pet=pet)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_pet(id)
    db = get_db()
    db.execute('DELETE FROM pet WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('pet.index'))