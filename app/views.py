from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/etablissement')
def etablissement():
    return render_template("views/add_etablissement.html")
