from flask import Blueprint, render_template
import logging
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/get/post')
def loader_page():
    return render_template("post_form.html")