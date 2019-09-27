from datetime import date

from flask import render_template
from flask_login import current_user,  login_required
from webapp.main import models
import os
from webapp.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    if not current_user.is_anonymous:
        user = {'username': current_user.username}
    else:
        user = {'username': 'Guest'}
    return render_template('index.html', title="Page d'accueil et menu", user=user,date=date.today())




@bp.route('/maliste')
@login_required
def maliste():
    maliste = os.listdir('c:/')
    return render_template('maliste.html', title='Madliste', myliste=maliste)


@bp.route('/madb')
def madb():
    liste = models.select_all()
    myliste = []
    for entiter in liste:
        myliste.append(entiter.lister())
    print(myliste)
    return render_template('madb.html', title='Madeb', mydbliste=myliste)

@bp.route('/test')
def test():
    return render_template('madb.html', title='Madeb', mydbliste=myliste)




