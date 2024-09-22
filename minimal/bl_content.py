from flask import (
    Blueprint, render_template, request, send_from_directory
)
from .layoutUtils import *
from .auth import *

bp = Blueprint('bl_content', __name__)

@bp.route('/', methods=('GET', 'POST'))
@manage_cookie_policy
def index():
    
    mc = set_menu("home") #to highlight menu option
    return render_template('content/index.html', mc=mc)

@bp.route('/project', methods=('GET', 'POST'))
@manage_cookie_policy
def project():
    
    mc = set_menu("") #to highlight menu option
    return render_template('content/project.html', mc=mc)

@bp.route('/design', methods=('GET', 'POST'))
@manage_cookie_policy
def design():

    mc = set_menu("design")
    return render_template('content/design.html', mc=mc)


@bp.route('/team',methods=('GET', 'POST'))
def team():

    mc = set_menu("")
    return render_template('content/team.html', mc=mc)


@bp.route('/experiment',methods=('GET', 'POST'))
def experiment():
    mc = set_menu("")
    return render_template('content/experiment.html', mc=mc)

@bp.route('/elsi',methods=('GET', 'POST'))
def elsi():
    mc = set_menu("")
    return render_template('content/elsi.html', mc=mc)


#MANAGE sitemap and robots calls 
#These files are usually in root, but for Flask projects must
#be in the static folder
@bp.route('/robots.txt')
@bp.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])

